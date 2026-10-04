"""
view_collapse_live.py
방금 내 컴퓨터에서 LLM이 실제로 생성한 날것의 답변(Raw Text)을
터미널에 그대로 띄워 거짓말 현장을 검증하는 스크립트
"""

import os
import sys
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def safe_print(*args, **kwargs):
    try:
        print(*args, **kwargs)
    except UnicodeEncodeError:
        safe_args = [
            str(a).encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8")
            for a in args
        ]
        print(*safe_args, **kwargs)

csv_path = "amazon_xai_audit_results.csv"
if not os.path.exists(csv_path):
    safe_print(f"[!] '{csv_path}' 파일이 없습니다. 먼저 파이프라인을 실행해 주세요.")
    sys.exit(1)

df = pd.read_csv(csv_path)

safe_print("\n" + "="*80)
safe_print("       🕵️ [현장 검증] 방금 내 컴퓨터의 Groq LLM이 뱉어낸 '날것의 원문' 확인")
safe_print("="*80)
safe_print("아래 내용은 제가 작성한 것이 아니라, 방금 유저분께서 VS Code에서 돌리셨을 때")
safe_print(f"Groq의 실제 LLM이 생성하여 '{csv_path}'에 저장된 100% 날것(Raw) 데이터입니다.\n")

for idx, row in df.iterrows():
    safe_print(f"{'#'*80}")
    safe_print(f"▶ [사건 #{idx+1}] 유저 ID: {row['user_id']}")
    safe_print(f"  - 고객 성향: {row['persona_role']}")
    safe_print(f"  - 고객의 절대 규칙: {row['hard_constraints']}")
    safe_print(f"  - 대상 제품: {row['product_title']}")
    safe_print(f"{'#'*80}")

    safe_print("\n[1단계: 원본 제품(x)을 줬을 때 LLM의 실제 원문 답변]")
    safe_print(f"  * 판정: {row['orig_decision']}")
    safe_print(f"  * LLM의 실제 답변:\n    \"{row['orig_reasoning']}\"")

    safe_print("\n[2단계: 우리가 몰래 가한 LIME 미세 섭동 공격 (z')]")
    safe_print(f"  * 우리가 제품 스펙을 이렇게 망가뜨렸음:\n    👉 {row['perturbation_desc']}")

    safe_print("\n[3단계: 망가진 스펙을 본 LLM의 실제 원문 답변 (💥 거짓말의 순간)]")
    safe_print(f"  * 판정: {row['pert_decision']}")
    safe_print(f"  * LLM의 실제 답변:\n    \"{row['pert_reasoning']}\"")

    safe_print("\n[4단계: XAI 판정관(Judge)의 현장 적발 보고서]")
    safe_print(f"  * 사후 정당화 적발 여부: {row['is_post_hoc_rationalized']} (True = 거짓말 적발!)")
    safe_print(f"  * 최종 판정: {row['verdict']} (충실도 점수: {row['faithfulness_score']} / 1.0)")
    safe_print(f"  * 적발된 거짓말 내용:\n    👉 \"{row['fabricated_excuse']}\"")
    safe_print(f"  * 감사관 종합 분석:\n    \"{row['audit_rationale']}\"")
    safe_print("\n" + "-"*80 + "\n")
