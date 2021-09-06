#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list has a cycle in it.
 *
 * @list: the singly linked list to be checked
 *
 * Return: to return 0 if there is no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *current;
if (list == NULL)
return (0);
current = list->next;
while (current != NUL)
{
if (current == list)
return (1);
current = current->next;
}
return (0);
}
