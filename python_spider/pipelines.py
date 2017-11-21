# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
from scrapy.utils.python import to_bytes


class JsonExporterPipeline:
    # 调用 scrapy 提供的 json exporter 导出 json 文件
    def __init__(self):
        self.file = open('./data/data.json', 'wb')
        # 初始化 exporter 实例，执行输出的文件和编码
        self.exporter = JsonLinesItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        # 开启写入
        self.exporter.start_exporting()
        self.exporter.export_empty_fields = True

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class JsonExporterPipelines(JsonLinesItemExporter):
    # 调用 scrapy 提供的 json exporter 导出 json 文件
    def __init__(self):
        # super(JsonExporterPipelines,self).__init__(self.file)
        JsonLinesItemExporter.__init__(self,file)
        self.file = open('./data/data.json', 'wb')
        # 初始化 exporter 实例，执行输出的文件和编码
        # self.exporter = JsonLinesItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        # 开启写入
        self.start_exporting()
        # self.exporter.export_empty_fields = True
        self.first_item = True

    def close_spider(self, spider):
        self.finish_exporting()
        self.file.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.export_item(item)
        return item

    def start_exporting(self):
        self.file.write(b"[\n")

    def finish_exporting(self):
        self.file.write(b"\n]")

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(b',\n')
        itemdict = dict(self._get_serialized_fields(item))
        data = self.encoder.encode(itemdict)
        self.file.write(to_bytes(data, self.encoding))