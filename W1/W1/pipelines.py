# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
import csv
# from bson.objectid import ObjectId
# useful for handling different item types with a single interface


class JsonDBHomedyPipeline:
    def __init__(self):
        self.data = []

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item

    def open_spider(self, spider):
        self.file = open('homedy.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        json.dump(self.data, self.file, ensure_ascii=False, indent=4)
        self.file.close()


# class CSVDBUnitopPipeline:
#     def process_item(self, item, spider):
#         self.file = open('coursedata.csv','a',newline='',encoding='utf-8')
#         # self.csv_writer = csv.DictWriter(self.file,delimiter="$", fieldnames=['coursename', 'lecturer', 'intro', 'describe','num_vote','rating','oldfee','newfee', 'lesson_num','courseUrl'])
#         # self.csv_writer.writerow(item)
#         self.csv_writer = csv.writer(self.file,delimiter="$")
#         self.csv_writer.writerow([item['coursename'], item['lecturer'], item['intro'], item['describe'],item['num_vote'],item['rating'],item['newfee'],item['oldfee'],item['lesson_num'],item['courseUrl']])
#         self.file.close
#         return item
    
