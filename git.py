'''
git  代码协同管理工具
  代码管理工具作用
    * 防止代码丢失，做备份
    * 代码版本的管理，可以进行多个节点的备份，在多个版本之间跳跃
    * 可以方便的将代码在多人之间进行共享传输
    * 多人开发时有各种模式可以方便代码管理

什么是git
  git是一个开源的分布式版本控制系统，可用于高效的管理大小项目。

分布式和集中式
  分布式： 每个节点都保存完成的代码，没有明确的中央服务器,节点之间项目推送下载代码完成代码共享. eg: GIT
  集中式： 代码集中管理，每次完成的代码上传到中央管理器,然后再统一从中央管理器下载代码使用. eg: SVN

git特点
  * git可以管理各种文件，特别是代码项目，多在*nix系统中使用
  * 是分布式管理，不同于集中式，这是git和svn的核心区别
  * git可以更好的支持分支，方便多人协同工作
  * git分布式代码更安全，有全球唯一的commit版本号
  * git是开源的系统
  * 使用git可以脱网工作，且数据传输速度较快

git安装
  linux :
    sudo apt-get install git

  windows : msysgit.github.io

git  配置命令
  git config

  配置级别
   1. 系统中所有的用户都可使用该配置
      命令 ： git config  --system [选项]
      配置文件： /etc/gitconfig

   2. 当前用户可使用该配置
      命令 ： git config  --global [选项]
      配置文件： ~/.gitconfig

   3. 当前项目可使用该配置
      命令 ： git config
      配置文件： project/.git/config

配置内容：
   1. 配置用户名
      e.g.  配置用户名为Tedu
      sudo git config --system user.name Tedu
   2. 配置用户邮箱
      e.g.  配置邮箱
      git config --global user.email lvze@tedu.cn
   3. 配置编译器
      e.g.  配置编译器
      git config core.editor pycharm
   4. 查看配置信息
      git config --list

git基本命令
  初始化仓库
    git init
   * 在某个项目目录下初始化仓库后会自动产生.git目录,该项目目录下工作的所有文档即可以使用git进行管理,
     该项目目录为git根目录
 在git工作目录下执行
  查看分支状态
    git status
   * 默认工作分支为master,可通过创建新的分支切换

  文件提交
    git  add   [file]
   * 将文件提交到暂存区
   * 提交内容可以是一个文件，多个文件用个空格分开
   * 如果是 * 表示所有文件，也可以是目录, *不包含隐藏文件, 若要提交隐藏文件需单独提交

  删除暂存区某个文件提交记录
    git rm --cached Readme.txt

文件同步到本地仓库
   git commit -m "some message"

   * 同步时需要附加一些同步信息 在-m后添加
   * 所有对工作区的修改如果想同步到本地仓库，都需要add--->commit

查看commit日志
    git log
    git log  --pretty=oneline

一些工作区命令
    查看本地文件和工作区差异
    git  diff   file

    从本地仓库恢复文件
    git checkout file

    丢弃工作区修改
    git checkout -- file

本地仓库文件的移动和删除
     移动文件
     git  mv   file  dir

     删除文件
     git  rm   file

     * 用法和mv rm命令相同。操作后直接commit即可工作区和本地仓库同步

  * 忽略文件
    在git仓库中有时候不需要把所有文件都进行协同操作,创建 .gitignore 文件夹,把忽略的文件名添加进去，这样在同步的时候就不会自动上传。

版本控制命令

回到之前版本
   git reset --hard HEAD^
   * HEAD后的^数量决定了回到上几个版本

   git reset --hard  commit_id
   * 使用commit前7位即可，回到指定的版本

去往更新的版本
   1. 查看所有历史版本号
      git  reflog
   2. 使用git reset 去往指定版本

   * git reflog 会有所有的操作记录,最新的操作时钟在最上边


标签管理

什么是标签 ： 即在当前工作位置添加快照，保存工作状态，一般用于版本的迭代。

创建新的标签
    git  tag  v1.0

    * 默认在最新的commit_id处打标签

    添加标签信息
    git  tag v1.0  -m  "message"

    指定某个commit_id打标签
    git  tag  v0.9  [commit_id]

查看标签
    git  tag    #列出当前标签
    git show v1.0  #显示标签具体信息

删除标签
    git  tag -d  v1.0

去往某个标签版本
    git reset --hard  v0.9

保存工作区
  1.工作区保存
    git stash save [message]
    说明: 将工作区未提交的修改封存,让工作区回到修改前的状态
  2.查看工作区列表
    git stash list
    说明: 最新保存的工作区在最上面
  3.应用某个工作区
    git stash apply [stash@{n}]
  4.删除工作区
    git stash drop [stash@{n}] 删除某一个工作区
    git stash clear 删除所有保存的工作区

分支操作
  什么是分支？
    分支即每个人获取原有代码,在此基础上创建自己的工作环境,单独开发,
    会影响其他分支的操作.开发完成后再统一合并到主线分支中.
  分支的好处：安全，不影响其他人工作，自己控制进度

查看当前分支
    git  branch
    * 前面有 * 号的分支表示当前正在工作的分支

创建分支
    git branch  [branch_name]

切换工作分支
    git checkout [branch]

创建并切换到新的分支
    git checkout -b [branch_name]

分支合并
    将某个分支合并到当前分支
    git merge  [branch]

    * 合并过程中如果没有冲突则直接合并后当前分支即为干净的状态
    * 如果产生冲突则需要人为选择然后在进行add---commit等操作
    * 在创建分支前尽量保证当前分支是干净点，以减少冲突的发生

删除分支
    git branch -d [branch_name]

    强制删除没有合并的分支
    git branch -D [branch_name]


远程仓库
    远程仓库： 远程主机上的仓库,实际上git是分布式的,每一台主机的git结构都相似,
    只是把其他主机的git仓库叫做远程而已.

创建共享仓库
    1. 创建文件夹
       mkdir  gitrepo
    2. 设置文件夹属主
       chown tarena:tarena gitrepo
    3. 将该文件夹设置为可共享的git仓库
       cd gitrepo
       git init  --bare  fly.git
    4. 设置本地仓库属主
       chown -R tarena:tarena fly.git

添加远程仓库
  git remote add origin tarena@127.0.0.1:/home/tarena/AID1807/gitrepo/fly.git
  * 默认使用SSH作为传输手段
  * 必须在本地的某个git仓库下执行才能使本地仓库和远程仓库关联

  git remote 查看当前远程仓库

删除远程主机
  git remote  rm  [origin]

将本地分支推送到远程
  git push -u origin master
  git push
  * 在第一次向远程仓库推送时需要加 -u选项,以后就不需要了

删除远程分支
  git push origin --delete 分支名

将本地标签推送到远程
  git push origin --tags  # 将本地所有标签推送

删除远程仓库标签
  git push origin --delete tag v1.0

从远程仓库获取项目
  git clone  tarena@127.0.0.1:/home/tarena/AID1807/gitrepo/fly.git

从远程仓库拉取分支或代码
  直接拉取远程分支和当前工作分支合并
  git pull origin dev_Tom

  拉取远程分支到本地，不合并
  git pull origin  dev_Tom     :   dev_Tom
                  远程分支名      本地分支名

  git branch -a  查看所有分支(包含远程)

代码退出和拉取
    将本地代码推送到连接的远程仓库
    git  push
    git push  --force  origin (当本地版本比远程版本旧是用本地旧版本覆盖远程                            新版本)

    从远程仓库更新代码
    git  pull
    git  fetch  （如果有新的分支拉取到本地不会和本地分支合并）

github
  github是一个开源项目社区网站。拥有全球最多的开源项目。开发者可以注册这个网站建立自己的github仓库。
  然后就可以在本地通过git像操作远程仓库一样操作github仓库。

  git是github唯一指定的代码管理工具

  网址：https://github.com/

  添加ssh秘钥
    1. 在本地主机生成ssh密钥对
      ssh-keygen

      * 默认密钥对存放在 ~/.ssh/ 下
      * 生成过程会提示设置密码，如果直接回车则表示不设置密码

    2. 进入 ~/.ssh 目录 复制 id_rsa.pub 公钥内容
    3. 登录github账号
       右上角头像下拉菜单--》settings --》
       左侧 SSH and GPG keys --》new ssh key --》填写title，将复制内容加入key文本框 点击add...

创建新的github仓库
  右上角 + 下拉菜单 --》 new repository --》 填写参考名和基本描述 ，根据情况选择是否添加readme等内容，选择共有还是私有 --》 点击创建

操作github仓库
  1.git remote 连接远程github仓库 如果需要输入密码输入github密码即可
  2. 使用git push等操作远程仓库的方法操作即可

PIP的使用

作用 ： 管理python的标准第三方库中第三方软件包

安装： sudo apt-get install python3-pip

常用命令：

    安装软件： pip3  install  [package]

      e.g.   sudo  pip3 install  ssh

    查看当前python软件包 ： pip3 list

    搜索某个名字的python包：pip3 search  [name]

    查看软件包信息：pip3  show  [package]

    升级软件包： pip3 install --upgrade [package]

    卸载软件包： sudo pip3  uninstall  [package]
        e.g.  sudo pip3 uninstall ssh

    导出软件包环境：pip3 freeze > requirements.txt

    根据文档自动安装:pip3 install -r requirements.txt


PDB调试方法

import  pdb

功能 ： 断点设置，单步执行， 查看代码，查看函数，追         踪变量等

命令：
  b  break     设置断点
  c  continue   继续执行
  n  next     单步执行
  s  step     单步执行，可以进入函数内部
  l  list     查看代码段
  pp          查看某个变量值
  help        帮助
  exit        退出pdb调试

进入pdb调试模式： pdb.set_trace()

直接进入PDB调试模式运行 ： python3 -m pdb debug.py




'''
