# blog2
开发环境：Python3.5 Django2.2
（开发步骤/详情）

### 设计博客模型：  

&emsp;文章标题——文本类型  
&emsp;文章摘要——文本类型  
&emsp;文章内容——文本类型  
&emsp;唯一ID标记——int数字类型（自增、主键）  
&emsp;发布日期——日期类型  
### 模型层定义字段  
&emsp;数字类型：IntegerField  
&emsp;文本类型：TextField  
&emsp;日期类型：DateTimeField  
&emsp;自增ID：AutoField  
&emsp;主键定义：primary_key属性  
### 使用Django Shell创建一篇文章

### Django Admin 模块
### 创建超级用户
### 在admin.py中调用模型 
from (app-name).models import your-model-name
### 然后将模型注册到admin模块里面 
&emsp;admin.site.register(your-model-name)
### 想要返回title-name  
&emsp;模型中定义__str__  return self.title


### 实现博客数据返回页面
&emsp;注：视图函数名不可与路由名相同


### 使用bootstrap实现静态博客页面
`bootcss.com/起步`

### 使用模板系统渲染博客页面
&emsp;——博客首页
&emsp;——文章详情页


### 实现文章详情页面的跳转
&emsp;——文章详情页url设计  
&emsp;——首页跳转&右侧最新文章跳转  

### 实现上下篇文章跳转
`boocss.com/组件/分页/翻页`


### 实现分页功能
&emsp;——bootstrap实现分页按钮bootcss.com/组件/分页/默认分页  
&emsp;——设计分页url  
&emsp;——使用django分页组件实现分页功能  

### 实现最新文章列表
