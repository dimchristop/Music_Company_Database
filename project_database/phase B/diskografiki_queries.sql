


1
SELECT hxografisi.τραγούδι,καλλιτεχνικό_όνομα FROM ermineuths inner join ergazetai 
on ermineuths.Αρ_ταυτ=ergazetai.Αρ_ταυτ
inner join hxografisi on ergazetai.κωδ_ηχογράφησης=hxografisi.κωδικός_ηχογράφησης
group by hxografisi.τραγούδι
order by καλλιτεχνικό_όνομα

poio tragoudi anhkei se poion kallitexnh


2
select ergazomenos.Αρ_ταυτ,Όνομα,τηλέφωνο,μισθός,mousikos.κατηγορία_μουσικής,mousikos.είδος from ergazomenos 
inner join mousikos on ergazomenos.Αρ_ταυτ=mousikos.Αρ_ταυτ  
WHERE κατηγορία_μουσικής LIKE '%Rock%' and( είδος like '%guitar%' or είδος like '%composer%'  or είδος like '%songwriter%')

vriskei mousikous me ta xaraktiristika pou theloume




3
SELECT distinct ergazomenos.Όνομα,ergazomenos.μισθός,ermineuths.καλλιτεχνικό_όνομα,ermineuths.αριθμός_βραβείων FROM ergazomenos 
inner join ermineuths on ergazomenos.Αρ_ταυτ=ermineuths.Αρ_ταυτ 
inner join kanei on ermineuths.Αρ_ταυτ=kanei.καλλιτέχνης 
inner join synavlia on kanei.όνομα=synavlia.τίτλος 
where έτος_υπογραφής_συμβολαίου+διάρκεια_συμβολαίου=2017 and synavlia.αριθμός_εισητηρίων>5000 and ermineuths.αριθμός_βραβείων>1

kritiria gia ypografi neou symvolaiou me ermineutes:eisitiria>5000 kai toulaxiston 1 vraveio




4
SELECT Όνομα_Τίτλος,Όνομα_καλλιτέχνη,αριθμός_τραγουδιών,πωλήσεις FROM paragwgh
where αριθμός_τραγουδιών=1
group by Όνομα_Τίτλος
order by πωλήσεις desc

emfanise ta singles me tis perissoteres pwlhseis




5
select χώρα,τοποθεσία,avg(αριθμός_εισητηρίων)  from synavlia
group by τοποθεσία
order by αριθμός_εισητηρίων desc

vriskei meso oro eisitiriwn gia kathe poli


6
SELECT paragwgh.Όνομα_Τίτλος ,paragwgh.αριθμός_τραγουδιών,sum(χρονική_διάρκεια) FROM hxografisi join apoteleitai ON hxografisi.κωδικός_ηχογράφησης=apoteleitai.κωδ_ηχογράφησης join paragwgh on apoteleitai.τίτλος_παραγωγής=paragwgh.Όνομα_Τίτλος 

group by paragwgh.Όνομα_Τίτλος 
order by sum(χρονική_διάρκεια)

vriskei gia kathe paragwgh poses wres hxografisis xreiasthkan






7
SELECT τραγούδι,count(κωδικός_ηχογράφησης) FROM `hxografisi` group by τραγούδι
having count(κωδικός_ηχογράφησης)>3

ta tragoudia pou xreiasthkan panw apo 3 hxografiseis gia na oloklhrwthoun


8
SELECT * FROM `ermineuths` where είδος_μουσικής LIKE '%Rock%' order by αριθμός_βραβείων desc

vrisei tous kalyterous kallitexnes Rock symfwna me ta vraveia









