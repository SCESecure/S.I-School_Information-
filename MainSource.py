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

print('시도교육청코드 : ' + jsonObj['ATPT_OFCDC_SC_CODE'])
print('시도교육청명 : ' + jsonObj['ATPT_OFCDC_SC_NM'])
print('표준학교코드 : ' + jsonObj['SD_SCHUL_CODE'])
print('학교명 : ' + jsonObj['SCHUL_NM'])
print('영문학교명 : ' + jsonObj['ENG_SCHUL_NM'])
print('학교종류명 : ' + jsonObj['SCHUL_KND_SC_NM'])
print('소재지명 : ' + jsonObj['LCTN_SC_NM'])
print('관할조직명 : ' + jsonObj['JU_ORG_NM'])
print('설립명 : ' + jsonObj['FOND_SC_NM'])
print('도로명우편번호 : ' + jsonObj['ORG_RDNZC'])
print('도로명주소 : ' + jsonObj['ORG_RDNMA'])
print('도로명상세주소 : ' + jsonObj['ORG_RDNDA'])
print('전화번호 : ' + jsonObj['ORG_TELNO'])
print('홈페이지주소 : ' + jsonObj['HMPG_ADRES'])
print('남녀공학구분명 : ' + jsonObj['COEDU_SC_NM'])
print('팩스번호 : ' + jsonObj['ORG_FAXNO'])
print('고등학교구분명 : ' + str(jsonObj['HS_SC_NM']))
print('산업체특별학급존재여부 : ' + jsonObj['INDST_SPECL_CCCCL_EXST_YN'])
print('고등학교일반실업구분명 : ' + jsonObj['HS_GNRL_BUSNS_SC_NM'])
print('특수목적고등학교계열명 : ' + str(jsonObj['SPCLY_PURPS_HS_ORD_NM']))
print('입시전후기구분명 : ' + jsonObj['ENE_BFE_SEHF_SC_NM'])
print('주야구분명 : ' + jsonObj['DGHT_SC_NM'])
print('설립일자 : ' + jsonObj['FOND_YMD'])
print('개교기념일 : ' + jsonObj['FOAS_MEMRD'])
print('수정일 : ' + jsonObj['LOAD_DTM'])