import requests, json, xmltodict

print('[S.I(School Information)]')
print('<본 프로그램은 API 키가 필요합니다. ("https://open.neis.go.kr/portal/mainPage.do"에서 발급 받을 수 있습니다.)>')

key = input('API 키 입력 : ')
inputstr = input('학교 입력 : ')

url = 'https://open.neis.go.kr/hub/schoolInfo?Type=xml&pIndex=1&pSize=100&' + key + '&' + 'SCHUL_NM=' + inputstr

content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['schoolInfo']['row'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

if len(jsonObj) > 1 :
    print('여러개의 학교가 감지되었습니다. 이름을 구체적으로 입력하여 주십시오.')

    exit()

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

print('어떤 기능을 사용하시겠습니까?')
print('1. 학교 기본 정보')
print('2. 급식 식단 정보')
maininput = input('입력 : ')

if maininput == '1' :
    print(schul_nm + '의 기본적인 정보는 다음과 같습니다.')
    print('')
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
    print('')
else :
    print('주어진 번호를 입력해주세요')