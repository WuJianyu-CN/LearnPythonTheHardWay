error: 无法推送一些引用到 'https://github.com/***'

提示：更新被拒绝，因为远程版本库包含您本地尚不存在的提交。这通常是因为另外
提示：一个版本库已向该引用进行了推送。再次推送前，您可能需要先整合远程变更
提示：（如 'git pull ...'）。
提示：详见 'Git push --help' 中的 'Note about fast-forwards' 小节。



原因可能是之前上传时创建的.git文件被删除或更改，或者其他人在github上提交过代码．

解决方案如下：１．强行上传　　 git push -u origin +master

　　　　　　　2． 尽量先同步github上的代码到本地，在上面更改之后再上传
