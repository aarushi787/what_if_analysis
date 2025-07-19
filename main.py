# # # # import json

# # # # # Load all JSON data
# # # # with open('scoring_DSAT_v2.json') as f:
# # # #     student_data = json.load(f)

# # # # with open('user_attempt_v2.json') as f:
# # # #     question_data = json.load(f)

# # # # with open('user_attempt_v3.json') as f:
# # # #     scoring_data = json.load(f)

# # # # # Sample print to verify loading
# # # # print("Student data sample:", student_data[:1])
# # # # print("Question metadata sample:", question_data[:1])
# # # # # print("Scoring map keys:", list(scoring_data.keys()))
# # # # print("Scoring map keys:", list(scoring_data[0].keys()))


# # # import json

# # # # Load the files
# # # with open('scoring_DSAT_v2.json') as f:
# # #     scoring_map = json.load(f)

# # # with open('user_attempt_v2.json') as f:
# # #     user_attempt = json.load(f)  # Change to user_attempt_v3.json for other student

# # # # Extract scoring map for "Reading and Writing"
# # # rw_map = next(x['map'] for x in scoring_map if x['key'] == "Reading and Writing")

# # # # Step 1: Count correct answers
# # # total_questions = 0
# # # correct_answers = 0

# # # for q in user_attempt:
# # #     if q['subject']['name'] == 'Reading and Writing':
# # #         total_questions += 1
# # #         if q['correct'] == 1:
# # #             correct_answers += 1

# # # # Step 2: Determine module2 difficulty (adaptive)
# # # threshold = 0.5  # 50% cutoff (adjustable)
# # # performance = correct_answers / total_questions
# # # module2_type = 'hard' if performance >= threshold else 'easy'

# # # # Step 3: Find final scaled score
# # # # NOTE: raw = correct_answers
# # # raw_score = correct_answers
# # # score_lookup = next((entry[module2_type] for entry in rw_map if entry['raw'] == raw_score), "N/A")

# # # # Print results
# # # print(f"\n✅ Total Questions: {total_questions}")
# # # print(f"✅ Correct Answers: {correct_answers}")
# # # print(f"✅ Module 2 Version: {module2_type.upper()}")
# # # print(f"✅ Final Scaled Score: {score_lookup}\n")


# # # # Step 4: Simulate fixing 1 incorrect answer
# # # what_if_correct = correct_answers + 1 if correct_answers < total_questions else correct_answers
# # # what_if_perf = what_if_correct / total_questions
# # # what_if_module = 'hard' if what_if_perf >= threshold else 'easy'
# # # what_if_score = next((entry[what_if_module] for entry in rw_map if entry['raw'] == what_if_correct), "N/A")

# # # print(f"🧪 What-If (Fix 1 answer):")
# # # print(f"    New Correct: {what_if_correct}")
# # # print(f"    Module 2: {what_if_module}")
# # # print(f"    New Score: {what_if_score}")

# # # DSAT What-If Score Analysis for Two Students

# # import json

# # def load_data():
# #     with open('scoring_DSAT_v2.json') as f:
# #         scoring_map = json.load(f)

# #     with open('user_attempt_v2.json') as f:
# #         user1 = json.load(f)

# #     with open('user_attempt_v3.json') as f:
# #         user2 = json.load(f)

# #     return scoring_map, user1, user2

# # def extract_score_map(scoring_map, subject_name):
# #     return next(x['map'] for x in scoring_map if x['key'] == subject_name)

# # def analyze_user(attempt_data, rw_map, threshold=0.5):
# #     total = 0
# #     correct = 0
# #     incorrect_qids = []

# #     for q in attempt_data:
# #         if q['subject']['name'] == 'Reading and Writing':
# #             total += 1
# #             if q['correct'] == 1:
# #                 correct += 1
# #             else:
# #                 incorrect_qids.append(q['question_id'])

# #     raw_score = correct
# #     performance = correct / total if total > 0 else 0
# #     module = 'hard' if performance >= threshold else 'easy'
# #     scaled_score = next((e[module] for e in rw_map if e['raw'] == raw_score), "N/A")

# #     return {
# #         "total": total,
# #         "correct": correct,
# #         "module": module,
# #         "scaled_score": scaled_score,
# #         "incorrect_qids": incorrect_qids
# #     }

# # def simulate_fix(attempt_data, rw_map, threshold=0.5):
# #     base = analyze_user(attempt_data, rw_map, threshold)
# #     if base['correct'] >= base['total']:
# #         return base  # already perfect

# #     new_correct = base['correct'] + 1
# #     new_performance = new_correct / base['total']
# #     new_module = 'hard' if new_performance >= threshold else 'easy'
# #     new_scaled_score = next((e[new_module] for e in rw_map if e['raw'] == new_correct), "N/A")

# #     return {
# #         "fixed_correct": new_correct,
# #         "new_module": new_module,
# #         "new_scaled_score": new_scaled_score,
# #         "gain": new_scaled_score - base['scaled_score'] if isinstance(new_scaled_score, int) else "N/A"
# #     }

# # def print_report(name, analysis, what_if):
# #     print(f"\n=== {name} ===")
# #     print(f"Total Questions: {analysis['total']}")
# #     print(f"Correct Answers: {analysis['correct']}")
# #     print(f"Module 2 Version: {analysis['module'].upper()}")
# #     print(f"Scaled Score: {analysis['scaled_score']}")
# #     print(f"Incorrect Questions: {len(analysis['incorrect_qids'])}")
# #     print(f"-- What-If Fixing 1 Wrong --")
# #     print(f"  New Correct: {what_if['fixed_correct']}")
# #     print(f"  New Module: {what_if['new_module']}")
# #     print(f"  New Scaled Score: {what_if['new_scaled_score']}")
# #     print(f"  Score Gain: {what_if['gain']}")

# # if __name__ == '__main__':
# #     scoring_map, user1_data, user2_data = load_data()
# #     rw_map = extract_score_map(scoring_map, "Reading and Writing")

# #     student1_analysis = analyze_user(user1_data, rw_map)
# #     student1_what_if = simulate_fix(user1_data, rw_map)

# #     student2_analysis = analyze_user(user2_data, rw_map)
# #     student2_what_if = simulate_fix(user2_data, rw_map)

# #     print_report("Student 1", student1_analysis, student1_what_if)
# #     print_report("Student 2", student2_analysis, student2_what_if)



# # DSAT What-If Score Analysis with Topic Breakdown, Multi-Fix Simulation, Export & Streamlit

# import json
# import pandas as pd
# from collections import Counter
# import streamlit as st

# THRESHOLD = 0.5  # Adaptive module threshold


# def load_data():
#     with open('scoring_DSAT_v2.json') as f:
#         scoring_map = json.load(f)

#     with open('user_attempt_v2.json') as f:
#         user1 = json.load(f)

#     with open('user_attempt_v3.json') as f:
#         user2 = json.load(f)

#     return scoring_map, user1, user2


# def extract_score_map(scoring_map, subject_name):
#     return next(x['map'] for x in scoring_map if x['key'] == subject_name)


# def analyze_user(attempt_data, subject, score_map, threshold=THRESHOLD):
#     total = 0
#     correct = 0
#     incorrect_qs = []
#     topic_counter = Counter()
#     incorrect_topics = Counter()

#     for q in attempt_data:
#         if q['subject']['name'] == subject:
#             total += 1
#             topic = q.get('topic', {}).get('name', 'Unknown')
#             topic_counter[topic] += 1
#             if q['correct'] == 1:
#                 correct += 1
#             else:
#                 incorrect_qs.append(q)
#                 incorrect_topics[topic] += 1

#     raw_score = correct
#     performance = correct / total if total > 0 else 0
#     module = 'hard' if performance >= threshold else 'easy'
#     scaled_score = next((e[module] for e in score_map if e['raw'] == raw_score), "N/A")

#     return {
#         "total": total,
#         "correct": correct,
#         "module": module,
#         "scaled_score": scaled_score,
#         "incorrect_qs": incorrect_qs,
#         "topic_breakdown": dict(topic_counter),
#         "topic_errors": dict(incorrect_topics)
#     }


# def simulate_multi_fix(analysis, score_map, threshold=THRESHOLD, fix_count=1):
#     base_correct = analysis['correct']
#     base_total = analysis['total']
#     new_correct = min(base_correct + fix_count, base_total)
#     new_perf = new_correct / base_total
#     new_module = 'hard' if new_perf >= threshold else 'easy'
#     new_scaled_score = next((e[new_module] for e in score_map if e['raw'] == new_correct), "N/A")
#     gain = new_scaled_score - analysis['scaled_score'] if isinstance(new_scaled_score, int) and isinstance(analysis['scaled_score'], int) else "N/A"

#     return {
#         "fixed_correct": new_correct,
#         "new_module": new_module,
#         "new_scaled_score": new_scaled_score,
#         "score_gain": gain
#     }


# def export_csv(results, filename='dsat_summary.csv'):
#     df = pd.DataFrame(results)
#     df.to_csv(filename, index=False)
#     print(f"✅ CSV exported: {filename}")


# def streamlit_ui(results):
#     st.title("DSAT Score Analyzer")
#     for res in results:
#         st.subheader(res['name'])
#         st.write(f"**Subject:** {res['subject']}")
#         st.write(f"Correct: {res['correct']} / {res['total']}")
#         st.write(f"Module 2: {res['module']}")
#         st.write(f"Scaled Score: {res['scaled_score']}")

#         st.markdown("**Topic Breakdown**")
#         for topic, total in res['topic_breakdown'].items():
#             errors = res['topic_errors'].get(topic, 0)
#             st.write(f"- {topic}: {total} total, {errors} incorrect")

#         st.markdown("**What-If Scenarios**")
#         for n, sim in res['simulations'].items():
#             st.write(f"Fixing {n} wrong → Score: {sim['new_scaled_score']} (+{sim['score_gain']})")


# if __name__ == '__main__':
#     scoring_map, user1_data, user2_data = load_data()
#     results = []

#     for name, user_data in {"Student 1": user1_data, "Student 2": user2_data}.items():
#         for subject in ["Reading and Writing", "Math"]:
#             score_map = extract_score_map(scoring_map, subject)
#             analysis = analyze_user(user_data, subject, score_map)
#             sims = {n: simulate_multi_fix(analysis, score_map, fix_count=n) for n in [1, 2, 3]}

#             results.append({
#                 "name": name,
#                 "subject": subject,
#                 "total": analysis['total'],
#                 "correct": analysis['correct'],
#                 "module": analysis['module'],
#                 "scaled_score": analysis['scaled_score'],
#                 "topic_breakdown": analysis['topic_breakdown'],
#                 "topic_errors": analysis['topic_errors'],
#                 "simulations": sims
#             })

#     # Export to CSV
#     export_csv([{k: v for k, v in r.items() if isinstance(v, (str, int))} for r in results])

#     # Streamlit app
#     try:
#         streamlit_ui(results)
#     except:
#         print("Run this script using `streamlit run main.py` to see the UI.")


# DSAT What-If Score Analysis with Topic Breakdown, Multi-Fix Simulation, Export & Streamlit

import json
import pandas as pd
from collections import Counter
import streamlit as st

THRESHOLD = 0.5  # Adaptive module threshold


def load_data():
    with open('scoring_DSAT_v2.json') as f:
        scoring_map = json.load(f)

    with open('user_attempt_v2.json') as f:
        user1 = json.load(f)

    with open('user_attempt_v3.json') as f:
        user2 = json.load(f)

    return scoring_map, user1, user2


def extract_score_map(scoring_map, subject_name):
    return next(x['map'] for x in scoring_map if x['key'] == subject_name)


def analyze_user(attempt_data, subject, score_map, threshold=THRESHOLD):
    total = 0
    correct = 0
    incorrect_qs = []
    topic_counter = Counter()
    incorrect_topics = Counter()

    for q in attempt_data:
        if q['subject']['name'] == subject:
            total += 1
            topic = q.get('topic', {}).get('name', 'Unknown')
            topic_counter[topic] += 1
            if q['correct'] == 1:
                correct += 1
            else:
                incorrect_qs.append(q)
                incorrect_topics[topic] += 1

    raw_score = correct
    performance = correct / total if total > 0 else 0
    module = 'hard' if performance >= threshold else 'easy'
    scaled_score = next((e[module] for e in score_map if e['raw'] == raw_score), "N/A")

    return {
        "total": total,
        "correct": correct,
        "module": module,
        "scaled_score": scaled_score,
        "incorrect_qs": incorrect_qs,
        "topic_breakdown": dict(topic_counter),
        "topic_errors": dict(incorrect_topics)
    }


def simulate_multi_fix(analysis, score_map, threshold=THRESHOLD, fix_count=1):
    base_correct = analysis['correct']
    base_total = analysis['total']
    new_correct = min(base_correct + fix_count, base_total)
    new_perf = new_correct / base_total
    new_module = 'hard' if new_perf >= threshold else 'easy'
    new_scaled_score = next((e[new_module] for e in score_map if e['raw'] == new_correct), "N/A")
    gain = new_scaled_score - analysis['scaled_score'] if isinstance(new_scaled_score, int) and isinstance(analysis['scaled_score'], int) else "N/A"

    return {
        "fixed_correct": new_correct,
        "new_module": new_module,
        "new_scaled_score": new_scaled_score,
        "score_gain": gain
    }


def export_csv(results, filename='dsat_summary.csv'):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"✅ CSV exported: {filename}")


def streamlit_ui(results):
    st.title("DSAT Score Analyzer")
    for res in results:
        st.subheader(res['name'])
        st.write(f"**Subject:** {res['subject']}")
        st.write(f"Correct: {res['correct']} / {res['total']}")
        st.write(f"Module 2: {res['module']}")
        st.write(f"Scaled Score: {res['scaled_score']}")

        st.markdown("**Topic Breakdown**")
        for topic, total in res['topic_breakdown'].items():
            errors = res['topic_errors'].get(topic, 0)
            st.write(f"- {topic}: {total} total, {errors} incorrect")

        st.markdown("**What-If Scenarios**")
        for n, sim in res['simulations'].items():
            st.write(f"Fixing {n} wrong → Score: {sim['new_scaled_score']} (+{sim['score_gain']})")


if __name__ == '__main__':
    scoring_map, user1_data, user2_data = load_data()
    results = []

    for name, user_data in {"Student 1": user1_data, "Student 2": user2_data}.items():
        for subject in ["Reading and Writing", "Math"]:
            score_map = extract_score_map(scoring_map, subject)
            analysis = analyze_user(user_data, subject, score_map)
            sims = {n: simulate_multi_fix(analysis, score_map, fix_count=n) for n in [1, 2, 3]}

            results.append({
                "name": name,
                "subject": subject,
                "total": analysis['total'],
                "correct": analysis['correct'],
                "module": analysis['module'],
                "scaled_score": analysis['scaled_score'],
                "topic_breakdown": analysis['topic_breakdown'],
                "topic_errors": analysis['topic_errors'],
                "simulations": sims
            })

    # Export to CSV
    export_csv([{k: v for k, v in r.items() if isinstance(v, (str, int))} for r in results])

    # Streamlit app
    try:
        streamlit_ui(results)
    except:
        print("Run this script using `streamlit run main.py` to see the UI.")
