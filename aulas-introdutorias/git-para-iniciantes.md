# Git para iniciantes

Criando repositório dentro da pasta do projeto:​

``` 
git init​
```

Para adicionar novos arquivos da pasta ao repositório:​

```
git add .​
```

Para "comitar" as mudanças no código:​

```
git commit –m "mensagem do commit"​
```

Para alterar o "branch" (ramo) principal do repositório para o padrão do github:​

```
git checkout  -M main​
```

Para subir com os commits para o repositório remoto (Ex: github):​

```
git push origin main (ou master se não for github)​
```

Criando nova branch:​

```
git branch nome_da_branch​
```

Mudando a branch corrente:​

```
git checkout nome_da_branch​
```

Adicionando as alterações de um branch ao principal:​

```
git checkout main​

git merge nome_do_branch_das_alterações​
```

​Adicionar um repositório remoto:​

```
git remote add url_do_repositório​
```

Alterar um repositório remoto:​

```
git remote set-url url_do_repositório​
```
Subir com as alterações para os repositórios remotos:​

```
git push origin nome_da_branch (se estiver trabalhando na main, git push origin main)​
```
​
Adicionando um repositório como um submodulo do projeto atual:

```
git submodule add url_do_repositório
```

Inicializando os submódulos:

```
git submodule init
```

Clonando e sincronizando os submódulos

```
git submodule update
git submodule sync
```