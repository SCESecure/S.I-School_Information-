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
	printf("�� ���α׷��� �¾� ���� ���ҷ� ���ǹǷ� ���� �ѹ� ���� �Ǵ� �⺻ ������ �ٲٰ� ���� �� ����Ͻñ� �ٶ��ϴ�.\n\n");

	printf("<API Ű�� �ʿ��մϴ�. (���̽� �������� ���� ���п��� �߱� ���� �� �ֽ��ϴ�.)>\n\n");
	printf("API Ű �Է� : ");
	gets(apikey);

	printf("\n�õ�����û�ڵ� �Է� (�ߺ��Ǵ� ��츸 �ش�, �ƴҽ� ����) : ");
	gets(atptcode);

	printf("\n�б� �Է� : ");
	gets(school_nm);

	printf("\n<�ð�ǥ ��� [���ڸ� �Է�]>\n");
	printf("\n�г⵵ �Է�(ex : 2021�г⵵) :  ");
	scanf("%d", &ay);
	
	printf("\n�б� �Է� : ");
	scanf("%d", &sem);
	fseek(stdin, 0, SEEK_SET);

	printf("\n�г� �Է� : ");
	scanf("%d", &grade);
	fseek(stdin, 0, SEEK_SET);

	printf("\n�� �Է� : ");
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

	printf("\n�¾� ������ �Ϸ��߽��ϴ�. ���� �� ���α׷��� �����ϼŵ� �����ϴ�. (�ƹ� Ű �Է�)\n");

	key = _getch();
	
	if (key > 0) {
		return 0;
	}
}