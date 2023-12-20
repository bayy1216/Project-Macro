from utils.write_utils import create_folder, create_file




def service_text(feat, package_name):
    txt = (f"package {package_name}.service.{feat}\n\n"
           f"import {package_name}.domain.{feat}.{feat.capitalize()}Repository\n"
           f"import org.springframework.transaction.annotation.Transactional\n"
           f"import org.springframework.stereotype.Service\n\n"
           f"@Service\n"
           f"@Transactional(readOnly = true)\n"
           f"class {feat.capitalize()}Service (\n"
           f"   private val {feat}Repository: {feat.capitalize()}Repository,\n"
           f"){{\n"
           f"\n}}")
    return txt

def controller_text(feat, package_name):
    txt = (f"package {package_name}.controller.{feat}\n\n"
           f"import {package_name}.service.{feat}.{feat.capitalize()}Service\n"
           f"import org.springframework.web.bind.annotation.*\n\n"
           f"@RestController\n"
           f"@RequestMapping(\"/{feat}\")\n"
           f"class {feat.capitalize()}Controller (\n"
           f"   private val {feat}Service: {feat.capitalize()}Service,\n"
           f"){{\n"
           f"\n}}")
    return txt


def entity_text(feat, package_name):
    txt = (f"package {package_name}.domain.{feat}\n\n"
           f"import javax.persistence.*\n\n"
           f"@Entity\n"
           f"class {feat.capitalize()} (\n"
           f"   @Id\n"
           f"   @GeneratedValue(strategy = GenerationType.IDENTITY)\n"
           f"   val id: Long? = null,\n"
           f"){{\n"
           f"\n}}")
    return txt

def repository_text(feat, package_name):
    txt = (f"package {package_name}.domain.{feat}\n\n"
           f"import org.springframework.data.jpa.repository.JpaRepository\n"
           f"import org.springframework.stereotype.Repository\n\n"
           f"interface {feat.capitalize()}Repository : JpaRepository<{feat.capitalize()}, Long> {{\n"
           f"\n}}")
    return txt

def create_feat(package_name_f, feat, folders_f):
    prefix = (f"./src/main/kotlin")
    package_name_origin = ""
    for a in package_name_f:
        package_name_origin += f"{a}."
    package_name_origin = package_name_origin[:-1]
    for x in package_name_f:
        prefix += f"/{x}"

    for f_module in folders_f:
        folder_name = f"./{prefix}/{f_module}/{feat}"
        create_folder(folder_name)
        if f_module == "controller":
            create_file(f"{folder_name}/{feat.capitalize()}Controller.kt", controller_text(feat, package_name_origin))
        elif f_module == "dto":
            create_folder(f"{folder_name}/request")
            create_folder(f"{folder_name}/response")
        elif f_module == "domain":
            create_file(f"{folder_name}/{feat.capitalize()}.kt", entity_text(feat, package_name_origin))
            create_file(f"{folder_name}/{feat.capitalize()}Repository.kt", repository_text(feat, package_name_origin))
        elif f_module == "service":
            create_file(f"{folder_name}/{feat.capitalize()}Service.kt", service_text(feat, package_name_origin))


if __name__ == "__main__":
    print("package 이름을 입력해주세요(com.example.app) : ", end="")
    package_name = input().split(".")




    print("생성할 feat를 입력해주세요(소문자) : ", end="")
    args = input().split()

    folders = ["controller", "domain", "dto", "service"]
    # 폴더 생성 함수 호출
    for feats in args:
        create_feat(package_name, feats, folders)
