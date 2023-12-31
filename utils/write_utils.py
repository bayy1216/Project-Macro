import os


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

def create_file(file_path, content):
    with open(file_path, "w") as file:
        # 파일에 쓸 내용 작성
        file.write(content)