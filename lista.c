#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define T 1000

struct line {
	struct line *next;
  int hora;
	char tarefa[T];
};

char* itoa(int i, char b[]){
    char const digit[] = "0123456789";
    char* p = b;
    if (i < 0) {
        *p++ = '-';
        i *= -1;
    }
    int shifter = i;
    do{
        ++p;
        shifter = shifter/10;
    }while(shifter);
    *p = '\0';
    do{
        *--p = digit[i%10];
        i = i/10;
    }while(i);
    return b;
}

struct line *ordemCrescente(struct line *p) {
    struct line *aux = p;
    struct line *t;
    int c;

    if (p == NULL || p->next == NULL)
        return NULL;

    while (aux != NULL) {
        t = aux->next;
        while (t != NULL) {
            if (aux->hora > t->hora) {
                c = aux->hora;
                aux->hora = t->hora;
                t->hora = c;
            }
            t = t->next;
        }
        aux = aux->next;
    }

    return p;
}

int enfileirar(struct line **fila, struct line **end, int hora_atual, char tarefa_atual[T])
{
		struct line *new = NULL;

		if (*fila == NULL) {
			new = (struct line *)malloc(sizeof(struct line));
			new->next = NULL;
			strcpy(new->tarefa, tarefa_atual);
	      		new->hora = hora_atual;
			*fila = new;
			*end = new;
		} else {
			new = (struct line *)malloc(sizeof(struct line));
			new->next = NULL;
			strcpy(new->tarefa, tarefa_atual);
     		 	new->hora = hora_atual;
			(*end)->next = new;
			*end = new;
		}

		return 0;
}

int split(char values[T], struct line **inicio)
{
	char tarefa_atual[T] = "\0", hora_atual[6] = "\0";
	int cont = 0, retorno = 0, size = strlen(values), flag = 0;
	struct line *init_aux = *inicio;
	struct line *end_aux = NULL;

	for (int i = 0; i < size; i++) {
		if (values[i] == ',' && flag == 0) {
			tarefa_atual[cont] = '\0';
			flag = 1;	
			cont = 0;
			continue;
		}else if (values[i] == ')' && flag == 1 ){
			hora_atual[cont] = '\0';
			flag = 0;
			int hora_int = atoi(hora_atual);
			enfileirar(&init_aux, &end_aux, hora_int, tarefa_atual);
			
			cont = 0;
			continue;
		}
		if (flag == 0){
			tarefa_atual[cont] = values[i];
			cont++;
		}else {
			hora_atual[cont] = values[i];
			cont++;
		}
	}
	*inicio = init_aux;
	return 0;
}
long calcularTamanhoArquivo(FILE *arquivo) {
 
    // guarda o estado ante de chamar a função fseek
    long posicaoAtual = ftell(arquivo);
	
    // guarda tamanho do arquivo
    long tamanho;
 
    // calcula o tamanho
    fseek(arquivo, 0, SEEK_END);
    tamanho = ftell(arquivo);
 
    // recupera o estado antigo do arquivo
    fseek(arquivo, posicaoAtual, SEEK_SET);
 
    return tamanho;
}

char * arquivo(char input_values[36]){
	int tamanho;

	FILE *archiv = fopen("output.txt", "r");
	
	tamanho = calcularTamanhoArquivo(archiv);
	
	fclose(archiv);

	archiv = fopen("output.txt", "r");

	for (int c = 0; c < tamanho; c++) {
		fscanf(archiv, "%c", &input_values[c]);
	}
	fclose(archiv);


	return input_values;
}

int main(void)
{
	char input_values[T] = "\0", *input;
	int retorno = 0, flag = 0, num[4];
	struct line *fila = NULL, *aux = NULL;

	input = arquivo(input_values);

	split(input, &fila);

	fila = ordemCrescente(fila);

	aux = fila;
	char h[4];

	printf(" ");

	while (aux != NULL) {
		printf("%s ", aux->tarefa);
		itoa(aux->hora, h);
		printf("às %c%c:%c%c\n", h[0], h[1], h[2], h[3]);
		aux = aux->next;
	}
	
	return 0;
}