from dbfread import DBF
import xlsxwriter, chardet

class converter():
    """
    Reads DBF file and writes it to excel book.

    """
        
    def encoding_detect(self):
        """
        Reads file in bytes, detects encoding.
        """
        
        with open('C:\\\\zakaz\\1.dbf', 'rb') as dbf_file:
            self.file_encoding = chardet.detect(dbf_file.read())['encoding']


    def dbf_to_xlsx(self):
        """
        Opens and read DBF file, using specified encoding in file_encoding
        variable, then 
        """

        workbook = xlsxwriter.Workbook('C:\\\\zakaz\\zakaz_dbf.xlsx')
        worksheet = workbook.add_worksheet()
        #formats
        header_format = workbook.add_format({'bold':False})
        
        column_letter = 65
        
        
        with DBF('C:\\\\zakaz\\1.dbf', encoding=self.file_encoding) as dbf_table:
            heads = list(list(dbf_table)[0].keys())
            for head in heads:
                worksheet.write(str(chr(column_letter)) + '1', head, header_format)
                column_letter += 1

            row = 1
            col = 0
            for record in dbf_table:
                for head in heads:
                    worksheet.write(row, col, record[head])
                    col += 1
                col = 0
                row += 1


if __name__ == '__main__':
    conv = converter()
    conv.encoding_detect()
    conv.dbf_to_xlsx()
