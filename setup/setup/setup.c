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

	FILE *fs = fopen("basicfile.txt", "w");

	printf("[S.I(School Information) Setup]\n\n");
	printf("본 프로그램은 셋업 파일 역할로 사용되므로 최초 한번 실행 또는 기본 내용을 바꾸고 싶을 때 사용하시길 바랍니다.\n\n");

	printf("<API 키가 필요합니다. (나이스 교육정보 개방 포털에서 발급 받을 수 있습니다.)>\n");
	printf("API 키 입력 : ");
	gets(apikey);

	fputs(apikey, fs);
	fputs("\n", fs);

	printf("\n시도교육청코드 입력 (중복되는 경우만 해당, 아닐시 무시) : ");
	gets(atptcode);

	fputs(atptcode, fs);
	fclose(fs);

	printf("\n<시간표 기능 [숫자만 입력]>\n");
	printf("학년도 입력(ex : 2021학년도) :  ");
	gets(ay);

	fputs(ay, fs);
	fclose(fs);
	
	printf("학기 입력 : ");
	gets(sem);

	fputs(sem, fs);
	fclose(fs);

	printf("학년 입력 : ");
	gets(grade);

	fputs(grade, fs);
	fclose(fs);

	printf("반 입력 : ");
	gets(class_nm);

	fputs(class_nm, fs);
	fclose(fs);

	FILE* fs2 = fopen("schoolfile.txt", "w");

	printf("\n학교 입력 : ");
	gets(school_nm);

	fputs(school_nm, fs2);
	fputs("\n", fs2);
	fclose(fs2);

	FILE* fs3 = fopen("isactive.txt", "w");
	fputs("active", fs3);
	fclose(fs3);

	printf("\n셋업 과정을 완료했습니다. 이제 이 프로그램은 종료하셔도 좋습니다. (아무 키 입력)\n");

	key = _getch();
	
	if (key > 0) {
		return 0;
	}
}