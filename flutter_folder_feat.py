import os
import sys


def create_folder(folder_path):
    try:
        # 디렉토리가 존재하지 않으면 생성
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"폴더 생성 성공: {folder_path}")
        else:
            print(f"폴더가 이미 존재합니다: {folder_path}")
    except Exception as e:
        print(f"폴더 생성 실패: {e}")

def create_feat(feat):
    create_folder(f"./{feat}")
    folders = ["component", "model", "provider","repository","view"]
    for f in folders:
        create_folder(f"./{feat}/{f}")

if __name__ == "__main__":
    args = sys.argv[1:]

    # 폴더 생성 함수 호출
    for feats in args:
        create_feat(feats)