import chilkat
import MySQLdb

spider = chilkat.CkSpider()
# semilla
spider.Initialize("http://elgourmet.com/actualidad/pagina-1")

spider.AddUnspidered("http://elgourmet.com/actualidad/pagina-1")
#
for i in range(0,300):

    success=spider.CrawlNext()

    if(success == True):
        print spider.lastUrl()
        print spider.lastHtmlTitle()
        print spider.lastHtmlDescription()
        print spider.lastHtmlKeywords()


        DB_HOST='127.0.0.1'
        DB_USER='root'
        DB_PASS='1234'
        BD_NAME='buscador'

        def run_query(query=''):
            datos=[DB_HOST,DB_USER,DB_PASS,BD_NAME]

            conn=MySQLdb.Connect(*datos)
            cursor=conn.cursor()
            cursor.execute(query)


            if query.upper().startswith('SELECT'):
                data=cursor.fetchall()
            else:
                conn.commit()
                data=None
            cursor.close()
            conn.close()

            return data

        url= spider.lastUrl()
        titulo= spider.lastHtmlTitle()
        pclav= spider.lastHtmlKeywords()
        descripcion= spider.lastHtmlDescription()
        visitas='1'

        dato=(url,titulo,pclav,descripcion,visitas)
        query="INSERT INTO clientapp_record(url,titulo,pclav,descripcion,visitas)VALUES('%s','%s','%s','%s','%s')"%dato
        run_query(query)

    else:
        if(spider.get_NumUnspidered()==0):
            print "No hay mas urls para rastrear"
        else:
            print spider.lastErrorText()


spider.sleepMs(5)
