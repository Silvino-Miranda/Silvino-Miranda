import os
import requests

# Defina o caminho base (ajuste conforme necessário)
base_path = r"c:\_Dev\Github\Pessoais\Silvino-Miranda"
assets_path = os.path.join(base_path, "assets", "images")

# Dicionário com categorias e suas imagens (URL e nome de arquivo)
images = {
    "stats": [
       ("https://github-readme-stats.vercel.app/api/top-langs/?username=Silvino-Miranda&layout=compact&langs_count=10", "top-langs.svg"),
       ("https://github-readme-stats.vercel.app/api?username=Silvino-Miranda&show_icons=true&include_all_commits=true&count_private=true", "github-stats.svg"),
    ],
    "programming_languages": [
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-plain.svg", "typescript-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg", "javascript-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg", "java-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/dart/dart-original.svg", "dart-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg", "python-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg", "csharp-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-plain.svg", "php-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg", "html5-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg", "css3-original.svg"),
    ],
    "frameworks": [
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-plain.svg", "nodejs-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/nestjs/nestjs-plain.svg", "nestjs-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg", "express-original-wordmark.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/spring/spring-original.svg", "spring-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/graphql/graphql-plain-wordmark.svg", "graphql-plain-wordmark.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/angularjs/angularjs-plain.svg", "angularjs-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/karma/karma-plain.svg", "karma-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg", "react-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/nextjs/nextjs-original-wordmark.svg", "nextjs-original-wordmark.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/codeigniter/codeigniter-plain.svg", "codeigniter-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain.svg", "bootstrap-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/flutter/flutter-original.svg", "flutter-original.svg"),
    ],
    "databases": [
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-plain.svg", "postgresql-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-plain.svg", "mysql-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/oracle/oracle-original.svg", "oracle-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-plain.svg", "mongodb-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/firebase/firebase-plain-wordmark.svg", "firebase-plain-wordmark.svg"),
    ],
    "devops": [
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg", "nginx-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg", "docker-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/jenkins/jenkins-original.svg", "jenkins-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/kubernetes/kubernetes-plain.svg", "kubernetes-plain.svg"),
    ],
    "tools": [
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/jira/jira-original.svg", "jira-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-plain.svg", "git-plain.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg", "github-original.svg"),
       ("https://raw.githubusercontent.com/devicons/devicon/master/icons/gitlab/gitlab-original.svg", "gitlab-original.svg"),
    ]
}

# Cria as pastas por categoria e baixa as imagens
for category, imgs in images.items():
    category_path = os.path.join(assets_path, category)
    os.makedirs(category_path, exist_ok=True)
    for url, filename in imgs:
        print(f"Baixando {filename} na categoria {category}...")
        try:
            response = requests.get(url)
            response.raise_for_status()
            file_path = os.path.join(category_path, filename)
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"{filename} salvo em {file_path}")
        except Exception as e:
            print(f"Erro ao baixar {url}: {e}")
