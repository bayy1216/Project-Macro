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


def create_file(file_path, content):
    with open(file_path, "w") as file:
        # 파일에 쓸 내용 작성
        file.write(content)


def screen_text(feat):
    txt = (f"import 'package:flutter/material.dart';\n\nclass {feat.capitalize()}Screen extends StatelessWidget {{\n"
           f"  const {feat.capitalize()}Screen({{Key? key}}) : super(key: key);\n\n"
           f"  @override\n  Widget build(BuildContext context) {{\n"
           f"    return const Container();\n  }}"
           f"\n}}")
    return txt


def create_feat(feat):
    create_folder(f"./{feat}")
    folders = ["component", "model", "provider", "repository", "view"]
    for f in folders:
        folder_name = f"./{feat}/{f}"
        create_folder(folder_name)
        if f == "repository":
            create_file(folder_name + f"/{feat}_repository.dart", f"class {feat.capitalize()}Repository {{\n\n}}")
        elif f == "view":
            create_file(folder_name + f"/{feat}_screen.dart", screen_text(feat))


if __name__ == "__main__":
    print("생성할 feat를 입력해주세요(소문자) : ", end="")
    args = input().split()

    # 폴더 생성 함수 호출
    for feats in args:
        create_feat(feats)
