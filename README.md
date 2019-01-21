# JavaDispatch
java package to war and dispatch to server 
Java打包和分发程序，为java tomcat项目提供web项目升级功能

使用场景：
			多个项目，布署在多台linux服务器上，每台服务器有不同的配置。每个项目需要针对每台
	服务器打包为不同的war包，打完包后，需要分发到服务器上，重启服务器。特别是需要
	每天重复打包和重启的重复工作，很适合用该项目。
	
	
项目工作原理：
			使用python3 django 在一台服务器上运行web项目，通过web界面按需要进行打包
	和分发到指定服务器，重启tomcat。
			服务器上运行django负责按需打包,每台tomcat服务器上运行一个python3 client客户端，负责
	接收服务器打好的war包其它命令，如tomcat重启或执行shell


项目安装：
			python3
			django
			
