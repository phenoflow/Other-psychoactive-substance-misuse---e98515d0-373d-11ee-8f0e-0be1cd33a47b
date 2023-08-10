# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"13c7.00","system":"readv2"},{"code":"13c8.00","system":"readv2"},{"code":"13c9.00","system":"readv2"},{"code":"13cA.00","system":"readv2"},{"code":"13cB.00","system":"readv2"},{"code":"13cC.00","system":"readv2"},{"code":"13cD.00","system":"readv2"},{"code":"13cJ.00","system":"readv2"},{"code":"13cK.00","system":"readv2"},{"code":"13r3.00","system":"readv2"},{"code":"13r4.00","system":"readv2"},{"code":"146F.00","system":"readv2"},{"code":"1V...00","system":"readv2"},{"code":"1V0..00","system":"readv2"},{"code":"1V00.00","system":"readv2"},{"code":"1V01.00","system":"readv2"},{"code":"1V04.00","system":"readv2"},{"code":"1V08.00","system":"readv2"},{"code":"1V09.00","system":"readv2"},{"code":"1V0B.00","system":"readv2"},{"code":"1V0C.00","system":"readv2"},{"code":"1V0E.00","system":"readv2"},{"code":"1V22.00","system":"readv2"},{"code":"1V23.00","system":"readv2"},{"code":"1V26.00","system":"readv2"},{"code":"1V3..00","system":"readv2"},{"code":"1V30.00","system":"readv2"},{"code":"1V31.00","system":"readv2"},{"code":"1V37.00","system":"readv2"},{"code":"1V38.00","system":"readv2"},{"code":"1V64.00","system":"readv2"},{"code":"7P22000","system":"readv2"},{"code":"8B23.00","system":"readv2"},{"code":"8B23.11","system":"readv2"},{"code":"8B23.13","system":"readv2"},{"code":"8B2N.00","system":"readv2"},{"code":"8B2P.00","system":"readv2"},{"code":"8B2Q.00","system":"readv2"},{"code":"8B2R.00","system":"readv2"},{"code":"8BA9.00","system":"readv2"},{"code":"8H7x.00","system":"readv2"},{"code":"9G23.00","system":"readv2"},{"code":"9G24.00","system":"readv2"},{"code":"E02..00","system":"readv2"},{"code":"E020.00","system":"readv2"},{"code":"E022.00","system":"readv2"},{"code":"E02y.00","system":"readv2"},{"code":"E02yz00","system":"readv2"},{"code":"E02z.00","system":"readv2"},{"code":"E24..00","system":"readv2"},{"code":"E24..11","system":"readv2"},{"code":"E240.00","system":"readv2"},{"code":"E240z00","system":"readv2"},{"code":"E242.00","system":"readv2"},{"code":"E242z00","system":"readv2"},{"code":"E243.00","system":"readv2"},{"code":"E243z00","system":"readv2"},{"code":"E247.00","system":"readv2"},{"code":"E247000","system":"readv2"},{"code":"E247100","system":"readv2"},{"code":"E247200","system":"readv2"},{"code":"E247300","system":"readv2"},{"code":"E247z00","system":"readv2"},{"code":"E248.00","system":"readv2"},{"code":"E248000","system":"readv2"},{"code":"E248100","system":"readv2"},{"code":"E248200","system":"readv2"},{"code":"E248300","system":"readv2"},{"code":"E248z00","system":"readv2"},{"code":"E249.00","system":"readv2"},{"code":"E249000","system":"readv2"},{"code":"E249100","system":"readv2"},{"code":"E249200","system":"readv2"},{"code":"E249300","system":"readv2"},{"code":"E249z00","system":"readv2"},{"code":"E24A.00","system":"readv2"},{"code":"E24z.00","system":"readv2"},{"code":"E25..00","system":"readv2"},{"code":"E258.00","system":"readv2"},{"code":"E258z00","system":"readv2"},{"code":"E259.00","system":"readv2"},{"code":"E259000","system":"readv2"},{"code":"E259100","system":"readv2"},{"code":"E259200","system":"readv2"},{"code":"E259300","system":"readv2"},{"code":"E259400","system":"readv2"},{"code":"E259z00","system":"readv2"},{"code":"E25y.00","system":"readv2"},{"code":"E25y000","system":"readv2"},{"code":"E25y100","system":"readv2"},{"code":"E25y200","system":"readv2"},{"code":"E25y300","system":"readv2"},{"code":"E25yz00","system":"readv2"},{"code":"E25z.00","system":"readv2"},{"code":"Eu11211","system":"readv2"},{"code":"Eu12211","system":"readv2"},{"code":"Eu14211","system":"readv2"},{"code":"Eu15211","system":"readv2"},{"code":"Eu16211","system":"readv2"},{"code":"Eu18211","system":"readv2"},{"code":"Eu19.00","system":"readv2"},{"code":"Eu19211","system":"readv2"},{"code":"Eu19500","system":"readv2"},{"code":"Eu19700","system":"readv2"},{"code":"Eu19z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-psychoactive-substance-misuse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["other-psychoactive-substance-misuse-drugrelated---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["other-psychoactive-substance-misuse-drugrelated---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["other-psychoactive-substance-misuse-drugrelated---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)