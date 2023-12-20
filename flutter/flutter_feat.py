from utils.write_utils import create_folder, create_file


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
