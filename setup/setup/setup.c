#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <conio.h>

int main() {
	
	char apikey[1000];
	char school_nm[1000];
	char atptcode[100];

	int key = 0;

	FILE *fs = fopen("basicfile.txt", "w");

	printf("[S.I(School Information) Setup]\n\n");
	printf("�� ���α׷��� �¾� ���� ���ҷ� ���ǹǷ� ���� �ѹ� ���� �Ǵ� �⺻ ������ �ٲٰ� ���� �� ����Ͻñ� �ٶ��ϴ�.\n\n");

	printf("<�� ���α׷��� API Ű�� �ʿ��մϴ�. (���̽� �������� ���� ���п��� �߱� ���� �� �ֽ��ϴ�.)>\n");
	printf("API Ű �Է� : ");
	gets(apikey);

	fputs(apikey, fs);
	fputs("\n", fs);

	printf("\n�õ�����û�ڵ� �Է� (�ߺ��Ǵ� ��츸 �ش�, �ƴҽ� ����) : ");
	gets(atptcode);

	fputs(atptcode, fs);
	fclose(fs);

	FILE* fs2 = fopen("schoolfile.txt", "w");

	printf("\n�б� �Է� : ");
	gets(school_nm);

	fputs(school_nm, fs2);
	fputs("\n", fs2);
	fclose(fs2);

	FILE* fs3 = fopen("isactive.txt", "w");
	fputs("active", fs3);
	fclose(fs3);

	printf("\n�¾� ������ �Ϸ��߽��ϴ�. ���� �� ���α׷��� �����ϼŵ� �����ϴ�. (�ƹ� Ű �Է�)\n");

	key = _getch();
	
	if (key > 0) {
		return 0;
	}
}