import os
import os.path
import requests
import xmltodict
import json

path1 = os.getcwd() + '\\basicfile.txt'
path2 = os.getcwd() + '\\schoolfile.txt'
path3 = os.getcwd() + '\\isactive.txt'

f = open(path3, mode='r', encoding='utf-8')
isactive = f.readline()

if isactive == 'deactive' :
    print('\n\n[셋업 프로그램에서 입력한 정보들이 존재하지 않습니다. 셋업 프로그램을 실행한 후 본 프로그램을 실행 바랍니다.]\n\n')

    exit()

print('[S.I(School Information)]\n')
print('<본 프로그램은 셋업 프로그램에서 입력한 정보들을 바탕으로 실행됩니다. 만약 수정을 원할시 셋업 프로그램을 실행바랍니다.>')
print('(주의 : 대학교는 지원이 되지 않습니다.)\n')

f = open(path1, mode='r', encoding='utf-8')
fkey = f.readline()
fatpt = f.readline()

f = open(path2, mode='r', encoding='cp949')
finputstr = f.readline()

key = fkey.strip('\n')
inputstr = finputstr.strip('\n')
atpt = fatpt.strip('\n')

# key = input('API 키 입력 : ')
# inputstr = input('학교 입력 : ')
# atpt = input('시도교육청코드 입력 (중복되는 경우만 해당, 아닐시 무시) : ')

url = 'https://open.neis.go.kr/hub/schoolInfo' + '?' + 'Type=xml&pIndex=1&pSize=100' + '&KEY=' + key \
     + '&SCHUL_NM=' + inputstr + '&ATPT_OFCDC_SC_CODE=' + atpt

content = requests.get(url).content
dict = xmltodict.parse(content)

try :
    tjsonString = json.dumps(dict['schoolInfo']['head'], ensure_ascii=False)
    tjsonObj = json.loads(tjsonString)

    if tjsonObj['list_total_count'] > '1' :
        print('\n' + tjsonObj['list_total_count'] + '개의 학교가 감지되었습니다. 해당하는 시도교육청코드를 셋업 파일에서 입력 바랍니다.\n')

        tjsonString = json.dumps(dict['schoolInfo']['row'])
        tjsonObj = json.loads(tjsonString)

        for output in tjsonObj :
            print(output['ATPT_OFCDC_SC_NM'] + ' : ' + output['ATPT_OFCDC_SC_CODE'])

        exit()
    elif tjsonObj['RESULT']['CODE'] != 'INFO-000' :
        print('\n' + tjsonObj['RESULT']['MESSAGE'])

        exit()

except KeyError :
    ejsonString = json.dumps(dict['RESULT'], ensure_ascii=False)
    ejsonObj = json.loads(ejsonString)

    print('\n' + ejsonObj['MESSAGE'])

    exit()

jsonString = json.dumps(dict['schoolInfo']['row'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

atpt_ofcdc_sc_code = jsonObj['ATPT_OFCDC_SC_CODE']
atpt_ofcdc_sc_nm = jsonObj['ATPT_OFCDC_SC_NM']
sd_schul_code = jsonObj['SD_SCHUL_CODE']
schul_nm = jsonObj['SCHUL_NM']
eng_schul_nm = jsonObj['ENG_SCHUL_NM']
schul_knd_sc_nm = jsonObj['SCHUL_KND_SC_NM']
lctn_sc_nm = jsonObj['LCTN_SC_NM']
ju_org_nm = jsonObj['JU_ORG_NM']
fond_sc_nm = jsonObj['FOND_SC_NM']
org_rdnzc = jsonObj['ORG_RDNZC']
org_rdnma = jsonObj['ORG_RDNMA']
org_rdnda = jsonObj['ORG_RDNDA']
org_telno = jsonObj['ORG_TELNO']
hmpg_adres = jsonObj['HMPG_ADRES']
coedu_sc_nm = jsonObj['COEDU_SC_NM']
org_faxno = jsonObj['ORG_FAXNO']
hs_sc_nm = jsonObj['HS_SC_NM']
indst_specl_ccccl_exst_yn = jsonObj['INDST_SPECL_CCCCL_EXST_YN']
hs_gnrl_busns_sc_nm = jsonObj['HS_GNRL_BUSNS_SC_NM']
spcly_purps_hs_ord_nm = jsonObj['SPCLY_PURPS_HS_ORD_NM']
ene_bfe_sehf_sc_nm = jsonObj['ENE_BFE_SEHF_SC_NM']
dght_sc_nm = jsonObj['DGHT_SC_NM']
fond_ymd = jsonObj['FOND_YMD']
foas_memrd = jsonObj['FOAS_MEMRD']
load_dtm = jsonObj['LOAD_DTM']

print('\n어떤 기능을 사용하시겠습니까?\n')
print('1. 학교 기본 정보')
print('2. 급식 식단 정보')
print('3. 학사 일정')
print('4. 학교 시간표 (초등학교, 중학교, 고등학교, 특수학교)')
maininput = input('입력 : ')

if maininput == '1' :
    print('\n\n' + schul_nm + '의 기본적인 정보는 다음과 같습니다.\n')
    print('시도교육청코드 : ' + atpt_ofcdc_sc_code)
    print('시도교육청명 : ' + atpt_ofcdc_sc_nm)
    print('표준학교코드 : ' + sd_schul_code)
    print('학교명 : ' + schul_nm)
    print('영문학교명 : ' + eng_schul_nm)
    print('학교종류명 : ' + schul_knd_sc_nm)
    print('소재지명 : ' + lctn_sc_nm)
    print('관할조직명 : ' + ju_org_nm)
    print('설립명 : ' + fond_sc_nm)
    print('도로명우편번호 : ' + org_rdnzc)
    print('도로명주소 : ' + org_rdnma)
    print('도로명상세주소 : ' + org_rdnda)
    print('전화번호 : ' + org_telno)
    print('홈페이지주소 : ' + hmpg_adres)
    print('남녀공학구분명 : ' + coedu_sc_nm)
    print('팩스번호 : ' + org_faxno)
    print('고등학교구분명 : ' + str(hs_sc_nm))
    print('산업체특별학급존재여부 : ' + indst_specl_ccccl_exst_yn)
    print('고등학교일반실업구분명 : ' + hs_gnrl_busns_sc_nm)
    print('특수목적고등학교계열명 : ' + str(spcly_purps_hs_ord_nm))
    print('입시전후기구분명 : ' + ene_bfe_sehf_sc_nm)
    print('주야구분명 : ' + dght_sc_nm)
    print('설립일자 : ' + fond_ymd)
    print('개교기념일 : ' + foas_memrd)
    print('수정일 : ' + load_dtm)

    exit()

elif maininput == '2' :
    print('\n\n')
    mlsv_ymd = input('급식 일자 입력(ex : 2000년 1월 1일 -> 20000101) : ')
    furl = 'https://open.neis.go.kr/hub/mealServiceDietInfo' + '?' + 'Type=xml&pIndex=1&pSize=100' + '&KEY=' + key \
        + '&ATPT_OFCDC_SC_CODE=' + atpt_ofcdc_sc_code + '&SD_SCHUL_CODE=' + sd_schul_code + '&MLSV_YMD=' + mlsv_ymd

    try :
        fcontent = requests.get(furl).content
        fdict = xmltodict.parse(fcontent)
        fjsonString = json.dumps(fdict['mealServiceDietInfo']['row'], ensure_ascii=False)
        fjsonObj = json.loads(fjsonString)

    except KeyError :
        fejsonString = json.dumps(fdict['RESULT'], ensure_ascii=False)
        fejsonObj = json.loads(fejsonString)

        print('\n' + fejsonObj['MESSAGE'])

        exit()

    print('\n' + schul_nm + '의 ' + mlsv_ymd + '일자 식단표는 다음과 같습니다.\n')
    fjsonObj['DDISH_NM'] = fjsonObj['DDISH_NM'].replace("<br/>", "\n")

    print(fjsonObj['DDISH_NM'])

    exit()

elif maininput == '3' :
    print('\n\n')
    aa_from_ymd = input('학사 시작 일자 입력(ex : 2000년 1월 1일 -> 20000101) : ')
    aa_to_ymd = input('학사 종료 일자 입력(ex : 2000년 1월 1일 -> 20000101) : ')

    acurl = 'https://open.neis.go.kr/hub/SchoolSchedule' + '?' + 'Type=xml&pIndex=1&pSize=100' + '&KEY=' + key \
        + '&ATPT_OFCDC_SC_CODE=' + atpt_ofcdc_sc_code + '&SD_SCHUL_CODE=' + sd_schul_code + '&AA_FROM_YMD=' + aa_from_ymd \
        + '&AA_TO_YMD=' + aa_to_ymd

    try :
        accontent = requests.get(acurl).content
        acdict = xmltodict.parse(accontent)
        acjsonString = json.dumps(acdict['SchoolSchedule']['row'])
        acjsonObj = json.loads(acjsonString)

    except KeyError :
        acjsonString = json.dumps(acdict['RESULT'])
        acjsonObj = json.loads(acjsonString)

        print('\n' + acjsonObj['MESSAGE'])

        exit()

    print('\n' + schul_nm + '의 학사 일정은 다음과 같습니다. (기간 : ' + aa_from_ymd + ' ~ ' + aa_to_ymd + ')\n')

    for acoutput in acjsonObj :
        print(acoutput['AA_YMD'] + ' : ' + acoutput['EVENT_NM'] + '[' + acoutput['SBTR_DD_SC_NM'] + ']')

    exit()

elif maininput == '4' :
    print('\n\n')
    print('<기간 입력>\n')
    all_ti_ymd = input('시간표 일자 입력(ex : 2000년 1월 1일 -> 20000101) : ')

    print('\n')
    print('<상세 입력>\n')
    print('[숫자만 입력 바랍니다.]\n')
    ay = input('학년도 입력 : ')
    sem = input('학기 입력 : ')
    grade = input('학년 입력 : ')
    class_nm = input('반 입력 : ')

    if schul_knd_sc_nm == '초등학교' :
        etiurl = 'https://open.neis.go.kr/hub/elsTimetable' + '?' + 'Type=xml&pIndex=1&pSize=100' + '&KEY=' + key \
            + '&ATPT_OFCDC_SC_CODE=' + atpt_ofcdc_sc_code + '&SD_SCHUL_CODE=' + sd_schul_code + '&ALL_TI_YMD=' + all_ti_ymd \
            + '&AY=' + ay + '&SEM=' + sem + '&GRADE=' + grade + '&CLASS_NM=' + class_nm

        try :
            eticontent = requests.get(etiurl).content
            etidict = xmltodict.parse(eticontent)
            etijsonString = json.dumps(etidict['elsTimetable']['row'])
            etijsonObj = json.loads(etijsonString)

        except KeyError :
            etiejsonString = json.dumps(etidict['RESULT'])
            etiejsonObj = json.loads(etiejsonString)

            print(etiejsonObj['MESSAGE'])

            exit()

        print('\n' + schul_nm + '의 ' + all_ti_ymd + '일자 시간표는 다음과 같습니다.')
        print('(제 ' + ay + '학년도 ' + sem + '학기 ' + grade + '학년 ' + class_nm + '반 시간표)\n')
        for etioutput in etijsonObj :
            print(etioutput['PERIO'] + '교시 : ' + etioutput['ITRT_CNTNT'])

        exit()

    elif schul_knd_sc_nm == '중학교' :
        mtiurl = 'https://open.neis.go.kr/hub/misTimetable' + '?' + 'Type=xml&pIndex=1&pSize=100' + '&KEY=' + key \
            + '&ATPT_OFCDC_SC_CODE=' + atpt_ofcdc_sc_code + '&SD_SCHUL_CODE=' + sd_schul_code + '&ALL_TI_YMD=' + all_ti_ymd \
            + '&AY=' + ay + '&SEM=' + sem + '&GRADE=' + grade + '&CLASS_NM=' + class_nm

        try :
            mticontent = requests.get(mtiurl).content
            mtidict = xmltodict.parse(mticontent)
            mtijsonString = json.dumps(mtidict['misTimetable']['row'])
            mtijsonObj = json.loads(mtijsonString)

        except KeyError :
            mtiejsonString = json.dumps(mtidict['RESULT'])
            mtiejsonObj = json.loads(mtiejsonString)

            print(mtiejsonObj['MESSAGE'])

            exit()

        print('\n' + schul_nm + '의 ' + all_ti_ymd + '일자 시간표는 다음과 같습니다.')
        print('(제 ' + ay + '학년도 ' + sem + '학기 ' + grade + '학년 ' + class_nm + '반 시간표)\n')
        for mtioutput in mtijsonObj :
            print(mtioutput['PERIO'] + '교시 : ' + mtioutput['ITRT_CNTNT'])

        exit()

    elif schul_knd_sc_nm == '고등학교' :
        htiurl = 'https://open.neis.go.kr/hub/hisTimetable' + '?' + 'Type=xml&pIndex=1&pSize=100' + '&KEY=' + key \
            + '&ATPT_OFCDC_SC_CODE=' + atpt_ofcdc_sc_code + '&SD_SCHUL_CODE=' + sd_schul_code + '&ALL_TI_YMD=' + all_ti_ymd \
            + '&AY=' + ay + '&SEM=' + sem + '&GRADE=' + grade + '&CLASS_NM=' + class_nm

        try :
            hticontent = requests.get(htiurl).content
            htidict = xmltodict.parse(hticontent)
            htijsonString = json.dumps(htidict['hisTimetable']['row'])
            htijsonObj = json.loads(htijsonString)

        except KeyError :
            htiejsonString = json.dumps(htidict['RESULT'])
            htiejsonObj = json.loads(htiejsonString)

            print(htiejsonObj['MESSAGE'])

            exit()

        print('\n' + schul_nm + '의 ' + all_ti_ymd + '일자 시간표는 다음과 같습니다.')
        print('(제 ' + ay + '학년도 ' + sem + '학기 ' + grade + '학년 ' + class_nm + '반 시간표)\n')
        for htioutput in htijsonObj :
            print(htioutput['PERIO'] + '교시 : ' + htioutput['ITRT_CNTNT'])

        exit()

else :
    print('주어진 번호를 입력해주세요')

    exit()
