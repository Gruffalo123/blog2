# blog2
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
