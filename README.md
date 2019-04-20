# blog2
（开发步骤/详情）

设计博客模型：
	文章标题——文本类型
	文章摘要——文本类型
	文章内容——文本类型
	唯一ID标记——int数字类型（自增、主键）
	发布日期——日期类型
模型层定义字段
	数字类型：IntegerField
	文本类型：TextField
	日期类型：DateTimeField
	自增ID：AutoField
	主键定义：primary_key属性
使用Django Shell创建一篇文章

Django Admin 模块
创建超级用户
在admin.py中调用模型 from (app-name).models import your-model-name
然后将模型注册到admin模块里面 admin.site.register(your-model-name)
想要返回title-name  模型中定义__str__  return self.title


实现博客数据返回页面
注：视图函数名不可与路由名相同


使用bootstrap实现静态博客页面
