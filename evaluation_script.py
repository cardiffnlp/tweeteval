# usage: evaluaton_script.py [-h] [--tweeteval_path TWEETEVAL_PATH]
#                            [--predictions_path PREDICTIONS_PATH] [--task TASK]

# optional arguments:
#   -h, --help: show this help message and exit
#   --tweeteval_path: Path to TweetEval dataset
#   --predictions_path: Path to predictions files
#   --task: Use this to get single task detailed results
#           (emoji|emotion|hate|irony|offensive|sentiment|stance)
#

from sklearn.metrics import classification_report
import argparse
import os

TASKS = [
    'emoji', 
    'emotion',
    'hate',
    'irony',
    'offensive',
    'sentiment',
    'stance']

STANCE_TASKS = [
    'abortion',
    'atheism',
    'climate',
    'feminist',
    'hillary']

def load_gold_pred(args):
    tweeteval_path = args.tweeteval_path
    predictions_path = args.predictions_path
    task = args.task

    if 'stance' in task:
        gold = []
        pred = []
        for stance_t in STANCE_TASKS:
            gold_path = os.path.join(tweeteval_path,task,stance_t,'test_labels.txt')
            pred_path = os.path.join(predictions_path,task,stance_t+'.txt')
            gold.append(open(gold_path).read().split("\n")[:-1])
            pred.append(open(pred_path).read().split("\n")[:-1])
        # flatten lists of lists
        gold = [p for each_target in gold for p in each_target]
        pred = [p for each_target in pred for p in each_target]
    else:
        gold_path = os.path.join(tweeteval_path,task,'test_labels.txt')
        pred_path = os.path.join(predictions_path,task+'.txt')
        gold = open(gold_path).read().split("\n")[:-1]
        pred = open(pred_path).read().split("\n")[:-1]
        
    return gold, pred

def single_task_results(args):
    task = args.task
    tweeteval_result = -1
    results = {}
    
    try:
        gold, pred = load_gold_pred(args)
        results = classification_report(gold, pred, output_dict=True)

        # Emoji (Macro f1)
        if 'emoji' in task:
            tweeteval_result = results['macro avg']['f1-score'] 

        # Emotion (Macro f1)
        elif 'emotion' in task:
            tweeteval_result = results['macro avg']['f1-score'] 

        # Hate (Macro f1)
        elif 'hate' in task:
            tweeteval_result = results['macro avg']['f1-score'] 

        # Irony (Irony class f1)
        elif 'irony' in task:
            tweeteval_result = results['1']['f1-score'] 

        # Offensive (Macro f1)
        elif 'offensive' in task:
            tweeteval_result = results['macro avg']['f1-score'] 

        # Sentiment (Macro Recall)
        elif 'sentiment' in task:
            tweeteval_result = results['macro avg']['recall']

        # Stance (Macro F1 of 'favor' and 'against' classes)
        elif 'stance' in task:
            f1_against = results['1']['f1-score']
            f1_favor = results['2']['f1-score']
            tweeteval_result = (f1_against+f1_favor) / 2
            
    except Exception as ex:
        print(f"Issues with task {task}: {ex}")
        
    return tweeteval_result, results

def is_all_good(all_tweeteval_results):
    return all([r != -1 for r in all_tweeteval_results.values()])


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='TweetEval evaluation script.')
    
    parser.add_argument('--tweeteval_path', default="./datasets/", type=str, help='Path to TweetEval datasets')
    parser.add_argument('--predictions_path', default="./predictions/", type=str, help='Path to predictions files')
    parser.add_argument('--task', default="", type=str, help='Indicate this parameter to get single task detailed results')

    args = parser.parse_args()

    if args.task == "":
        all_tweeteval_results = {}
        
        # Results for each task
        for t in TASKS:
            args.task = t
            all_tweeteval_results[t], _ = single_task_results(args)
            
        # Print results (score=-1 if some results are missing)
        print(f"{'-'*30}")
        if is_all_good(all_tweeteval_results):
            tweeteval_final_score = sum(all_tweeteval_results.values())/len(all_tweeteval_results.values())
        else:
            tweeteval_final_score = -1
        for t in TASKS:
            # Each score
            print(f"{t}: {all_tweeteval_results[t]}") 
        # Final score
        print(f"{'-'*30}\nTweetEval Score: {tweeteval_final_score}")
        
    else:
        # Detailed results of one single task (--task parameter)
        tweeteval_resut, results = single_task_results(args)
        for k in results:
            print(k, results[k])
        print(f"{'-'*30}\nTweetEval Score ({args.task}): {tweeteval_resut}")

