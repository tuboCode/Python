from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter

from urllib.request import urlopen

# 获取naacl06-shinyama.pdf文档对象
fp = open("naacl06-shinyama.pdf", "rb")

# fp = open("url")

# 创建一个文档关联的对象
parser = PDFParser(fp)

# pdf文档的对象
doc = PDFDocument()

# 连接解释器与文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
# 里面的参数为密码，此处密码为空
doc.initialize("")

# 创建pdf资源管理器
resource = PDFResourceManager()

# 参数分析器
laparam = LAParams()

# 创建一个聚合器
device = PDFPageAggregator(resource,laparams=laparam)

# 创建一个pdf页面解释器
interpreter = PDFPageInterpreter(resource,device)

# 使用文档对象得到页面的集合
for page in doc.get_pages():
    # 使页面解释器来读取
    interpreter.process_page(page)

    # 使用聚合器来获得内容
    layout = device.get_result()

    for out in layout:
        # 判断有没有get_text属性
        if hasattr(out, "get_text"):
            print(out.get_text())

