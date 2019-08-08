from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfparser import PDFParser, PDFDocument

def read_pdf(path):
    with open(path, 'rb') as pdf1:
        parser = PDFParser(pdf1)
    text = ""
    #PDf文档的对象
    doc = PDFDocument()
    #链接解释器和文档对象
    parser.set_document(doc)
    doc.set_parser(parser)
    #初始化文档
    doc.initialize("")
    #创建PDF资源管理器
    resource = PDFResourceManager()
    #参数分析器
    laparam = LAParams()
    #创建一个聚合器
    device = PDFPageAggregator(resource,laparams=laparam)
    #创建PDF页面解释器
    interpreter = PDFPageInterpreter(resource,device)
    #得到第一页
    for page in doc.get_pages():
    #使用页面解释器来读取
        interpreter.process_page(page)
    #使用聚合器来获得内容
        layout = device.get_result()
        for out in layout:
            if hasattr(out, 'get_text'):  # 需要注意的是在PDF文档中不只有 text 还可能有图片等等，为了确保不出错先判断对象是否具有get_text()方法
                text += out.get_text()
    text = text.split('\n')
    return text

if __name__ == '__main__':
    print(read_pdf(
        r'C:\Users\Kai Wang\Documents\test\latam\Individual Agreement -  IB_LATAM# 2290 -  IB# 0017 - 1563364360-ROlBb\Ronny Abel Tomala Cruz-Au10tix.pdf'
        )[0])