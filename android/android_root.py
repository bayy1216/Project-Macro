from utils.write_utils import create_folder, create_file


def repository_text(feat, package_name):
    txt = (f"package {package_name}.android.domain.{feat}\n\n"
           f"interface {feat.capitalize()}Repository {{\n"
           f"\n}}")
    return txt

def repository_impl_text(feat, package_name):
    txt = (f"package {package_name}.android.data.repository.{feat}\n\n"
           f"import {package_name}.android.domain.{feat}.{feat.capitalize()}Repository\n"
           f"import javax.inject.Inject\n\n"
           f"class {feat.capitalize()}RepositoryImpl @Inject constructor() : {feat.capitalize()}Repository {{\n"
           f"\n}}")
    return txt

def create_domain(feat, package_name):
    package_path = package_name.replace(".", "/")
    prefix = (f"./domain/src/main/kotlin/{package_path}/android/domain")
    domain_folders = ["model", "repository", "usecase", "params"]

    for folder in domain_folders:
        create_folder(f"{prefix}/{folder}/{feat}")
        if folder == "repository":
            create_file(f"{prefix}/{folder}/{feat}/{feat.capitalize()}Repository.kt", repository_text(feat, package_name))

def create_presentation(feat, package_name):
    package_path = package_name.replace(".", "/")
    prefix = (f"./presentation/src/main/kotlin/{package_path}/android/presentation")
    presentation_folders = ["view", "viewmodel", "component", "state"]

    for folder in presentation_folders:
        create_folder(f"{prefix}/{feat}/{folder}")

def create_data(feat, package_name):
    package_path = package_name.replace(".", "/")
    prefix = (f"./data/src/main/kotlin/{package_path}/android/data")
    data_folders = ["dto", "repository"]

    for folder in data_folders:
        folder_name = f"{prefix}/{folder}/{feat}"
        create_folder(folder_name)
        if folder == "dto":
            create_folder(f"{folder_name}/request")
            create_folder(f"{folder_name}/response")
        elif folder == "repository":
            create_file(f"{folder_name}/{feat.capitalize()}RepositoryImpl.kt", repository_impl_text(feat, package_name))

if __name__ == "__main__":
    print("package 이름을 입력해주세요(com.example.app) : ", end="")
    package_name = input()




    print("생성할 feat를 입력해주세요(소문자) : ", end="")
    args = input().split()


    for feat in args:
        create_data(feat, package_name)
        create_domain(feat, package_name)
        create_presentation(feat, package_name)
