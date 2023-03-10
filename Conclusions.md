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

  ```print``` 函数的结束操作 ```print(' ' end = '')``` 原有的print操作默认是换行，此处以指定的结束语句结束打印

- 逻辑运算符 ```and or not```
  
## 3rd Day

- ```range(start,stop,step)``` range函数的用法，截止到stop处停止，不会包含stop
- 取余函数 ```%```  其中 ```value%i```表示value除以i的余
- ```swap``` 函数在python中为```x,y=y,x```
- ```for``` 循环无相加操作

## 4th Day
- ```//``` 表示整数除法 返回商的整数部分

## 5th Day 
- ```from...import``` 引入库
- ```random randint ```随机数函数
- ```randint(x,y)```生成在两个数字之间的随机数
  
## 5th Day
- 函数的定义和封装

# 常见算法

- 回文数字：```while ( number >0 ) reserve = reserve * 10 + num%10  num=num//10```
- 