#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <conio.h>

int main() {
	
	char apikey[1000];
	char school_nm[1000];
	char atptcode[100];

	int ay;
	int sem;
	int grade;
	int class_nm;

	int key = 0;

	printf("[S.I(School Information) Setup]\n\n");
	printf("본 프로그램은 셋업 파일 역할로 사용되므로 최초 한번 실행 또는 기본 내용을 바꾸고 싶을 때 사용하시길 바랍니다.\n\n");

	printf("<API 키가 필요합니다. (나이스 교육정보 개방 포털에서 발급 받을 수 있습니다.)>\n\n");
	printf("API 키 입력 : ");
	gets(apikey);

	printf("\n시도교육청코드 입력 (중복되는 경우만 해당, 아닐시 무시) : ");
	gets(atptcode);

	printf("\n학교 입력 : ");
	gets(school_nm);

	printf("\n<시간표 기능 [숫자만 입력]>\n");
	printf("\n학년도 입력(ex : 2021학년도) :  ");
	scanf("%d", &ay);
	
	printf("\n학기 입력 : ");
	scanf("%d", &sem);
	fseek(stdin, 0, SEEK_SET);

	printf("\n학년 입력 : ");
	scanf("%d", &grade);
	fseek(stdin, 0, SEEK_SET);

	printf("\n반 입력 : ");
	scanf("%d", &class_nm);
	fseek(stdin, 0, SEEK_SET);

	FILE* fs1 = fopen("basicfile.json", "w");

	fprintf(fs1, "{\n");
	fprintf(fs1, "	\"Basic\": {\n");
	fprintf(fs1, "		\"apikey\": \"%s\",\n", apikey);
	fprintf(fs1, "		\"atptcode\": \"%s\",\n", atptcode);
	fprintf(fs1, "		\"school_nm\": \"%s\",\n", school_nm);
	fprintf(fs1, "		\"SC\": {\n");
	fprintf(fs1, "			\"ay\": \"%d\",\n", ay);
	fprintf(fs1, "			\"sem\": \"%d\",\n", sem);
	fprintf(fs1, "			\"grade\": \"%d\",\n", grade);
	fprintf(fs1, "			\"class_nm\": \"%d\"\n", class_nm);
	fprintf(fs1, "		}\n");
	fprintf(fs1, "	}\n");
	fprintf(fs1, "}");

	fclose(fs1);

	FILE* fs2 = fopen("isactive.json", "w");

	fprintf(fs2, "{\n");
	fprintf(fs2, "	\"Activation\": {\n");
	fprintf(fs2, "		\"isactive\": \"active\"\n");
	fprintf(fs2, "	}\n");
	fprintf(fs2, "}");

	fclose(fs2);

	printf("\n셋업 과정을 완료했습니다. 이제 이 프로그램은 종료하셔도 좋습니다. (아무 키 입력)\n");

	key = _getch();
	
	if (key > 0) {
		return 0;
	}
}