# NLP
learn nlp 

1.本地初始化git目录
git init

2.新建文件并且写入内容
touch a.txt
echo "new data" >> a.txt

3.添加到暂存区
git add .

git commit -m "a.txt"

4.添加远程仓库
git remote add origin https://gitee.com/jianan/learnGit.git

5.本地仓库也远程仓库关联
git branch --set-upstream-to=origin/master master
error: the requested upstream branch 'origin/master' does not exist
先执行git fetch

6.拉取远程仓库内容到本地
这时候用git pull会提示(毕竟本地和远程仓库没啥关系指针连接不起来的缘故吧)：
fatal: refusing to merge unrelated histories
因此命令应该改为：
git pull origin master --allow-unrelated-histories  

7.将最新的内容推送到远程仓库
git push
