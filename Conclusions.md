# 问题总结与解决
## Git
- Git的配置以及与远程仓库的链接
  ```git remote add origin git@github.com:username/project.git```
- 在本地仓库中提交
  
  ```git add .```  文件夹中全部提交 

  ```git add name.txt``` 提交指定文件夹

  ```git add nema1.txt name2.txt test/```   提交多个文件

  ```git commit -m"text"```

  ```git push origin main```

- GitHub默认分支为master分支，因此提交到main分支要进行修改。
- 在本地和GitHub中分别删除master分支即可
- 更新操作分别做取和推
  
  ```git pull ```

  ```git push```
- 切换工作分支与删除工作分支
  
  ```git check out main```

  ```git branch -D master```

##  VS code

- 解决在VS终端下zsh乱码问题：设置字体一致

  ```"terminal.integrated.fontFamily": "Hack Nerd Font",```

- 解决VS下终端输入问题：setting terminal设置问题

- 在VS下的部分代码报错：选择在Terminal中直接利用Python3运行

##  Terminal

- pip3的安装升级与更新
- Ipython的配置


# Python Learning

## 1st  Day  and  2ed  Day

- 输入输出函数 ```input()```  ```print()```
  
  输入为字符串型，可强制类型转换，python2不支持直接输入字符串，python3支持。
  
  语法检查十分严格，输入函数要空格。输出格式类似于传统高级语言。

  以及中文输入在源文件头部添加 ```coding=utf-8```

  ```f-string``` 函数的相关打印

- 逻辑运算符 ```and or not```
  
