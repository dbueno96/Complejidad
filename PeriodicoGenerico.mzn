int : pages;
enum topics;
array[topics] of int: mins; 
array[topics] of int: maxs;
array[topics] of int: readers;

array[topics] of var bool: includes;
array[topics] of var int: paginas; 

var int :f;

constraint forall(i in topics)
                    (paginas[i] <= maxs[i]);
constraint forall(i in topics)
                    (paginas[i]>= mins[i]);
constraint sum(i in topics)
                (includes[i]*paginas[i])  <=pages;
constraint f=sum(i in topics)
                (readers[i]*includes[i]*paginas[i]);
solve maximize f;


output ["_Temas : \(topics)\n",
        "_Páginas : \(paginas)\n",
        "_Includes : \(includes)\n",
        "_Readers : \(f)\n"];