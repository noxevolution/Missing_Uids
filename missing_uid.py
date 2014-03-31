g_list_imp_retail = []

'''
Read the ts-retail-offers file and find out Missing UIDS.
'''
def retail_ts_offers():
    global g_list_imp_retail

    lfilename = "ts_retail_offers.csv"
    
    fp_ts_retail = open("C:\\Users\\AKDANI\\Desktop\\New folder\\" + lfilename)
    fp_missing_uid = open("C:\\Users\\AKDANI\\Desktop\\New folder\\Missing_UID_" + lfilename, "w")
    
    l_header_line = fp_ts_retail.readline()
    fp_missing_uid.write(l_header_line)
    
    l_list_ts_retail = fp_ts_retail.readlines()
    
    for value in l_list_ts_retail:
        
        if value.split(",")[0].strip() not in g_list_imp_retail and len(value.split(",")[0]) > 0:
            fp_missing_uid.write(value)
            
    fp_missing_uid.close()
            
    return

'''
Read the imp consolidated file and store the Unique ID in a list.
'''
def imp_consolidate():
    global g_list_imp_retail
    
    fp_imp_consolidated = open("C:\\Users\\AKDANI\\Desktop\\New folder\\imp_consolidated.csv")
    
    l_header_line = fp_imp_consolidated.readline()
    
    l_list_imp_consolidated = fp_imp_consolidated.readlines()
    
    for value in l_list_imp_consolidated:
        if len(value.split(",")[0]) > 0:
            g_list_imp_retail.append(value.split(",")[0].strip())
    
    return

'''
Starting point of the Program.
'''
if __name__ == '__main__':
    imp_consolidate()
    retail_ts_offers()
    
    print "Done."
