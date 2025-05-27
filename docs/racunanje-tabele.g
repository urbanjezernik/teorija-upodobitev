# izračun tabele karakterjev dane končne grupe nad C
# s projekcijami na izotipične komponente

# grupa
g := AlternatingGroup(5);
# g := GL(2,3);
# x_gen := (1,3,5)(2,4,6)(7,11,9)(8,12,10); y_gen := (3,9,4,10)(5,7)(6,8)(11,12); g := Group([ x_gen, y_gen ]);

# naštejemo elemente grupe 
# in določimo predstavnike konjugiranostnih razredov
elementi := Elements(g);;
predstavniki_konj_razredov := List(ConjugacyClasses(g), Representative);;

# pripravimo prostor fun(G,C)
standardni_prostor := FullRowSpace( Rationals, Size(g) );;
standardna_baza := BasisVectors(Basis(standardni_prostor));;

# funkcija za izračun matrike regularne upodobitve elementa x
# v bazi karakterističnih funkcij 1_y
rho := function (x)
    local matrika, i, y, slika_1_y;
    matrika := [];
    for i in [1..Size(g)] do
        y := elementi[i];
        slika_1_y := standardna_baza[Position(elementi, y * x^(-1))];
        Append(matrika, [slika_1_y]);
    od;
    matrika := TransposedMat(matrika);
    return matrika;
end;

# funkcija za izračun Fourierove transformacije 
# 1_C karakteristične funkcije konjugiranostnega razreda
# v regularni upodobitvi
fourier_konj_razreda := function (c)
    return Sum(List(ConjugacyClass(g,c), x -> rho(x^(-1))));
end;

# določimo lastne podprostore Fourierovih transformacij 1_C
Print("Določanje lastnih podprostorov ...\n");
stevilo_konj_razredov := Length(predstavniki_konj_razredov);;
lastni_podprostori := [];;
indeks := 0;
for c in predstavniki_konj_razredov do
    indeks := indeks + 1;
    Print(indeks, "\t/", stevilo_konj_razredov, "\r");
    Append(lastni_podprostori, [Eigenspaces(CF(Exponent(g)), fourier_konj_razreda(c))]);
od;

# izračunamo netrivialne preseke lastnih podprostorov
# to so ravno vse izotipične komponente
Print("Določanje presekov lastnih podprostorov ...\n");
kandidati := lastni_podprostori[1];
indeks := 0;
for novi_podprostori in lastni_podprostori do
    indeks := indeks + 1;
    Print(indeks, "\t/", stevilo_konj_razredov, "\r");
    novi_kandidati := [];
    for kandidat in kandidati do
        for podprostor in novi_podprostori do
            nov_kandidat := Intersection(kandidat, podprostor);
            if Dimension(nov_kandidat) > 0 then
                Append(novi_kandidati, [nov_kandidat]);
            fi;
        od;
    od;
    kandidati := novi_kandidati;
od;
izotipicne_komponente := kandidati;

# funkcija za Gram-Schmidtovo ortogonalizacijo dane množice vektorjev
gram_schmidt := function (vektorji) 
    local nova_baza, n, m, dimenzije, i, j, projekcijski_skalar;
    # določimo dimenzijo vektorjev
    dimenzije := DimensionsMat(vektorji);
    m := dimenzije[1];
    n := dimenzije[2];
    # pripravimo matriko nove baze
    nova_baza := NullMat(m,n);
    nova_baza[1] := vektorji[1];
    # določimo novo bazo
    for i in [2..m] do
        nova_baza[i] := vektorji[i];
        for j in [1..i-1] do
            projekcijski_skalar := (ComplexConjugate(nova_baza[j]) * nova_baza[i]) / (ComplexConjugate(nova_baza[j]) * nova_baza[j]);
            nova_baza[i] := nova_baza[i] - projekcijski_skalar * nova_baza[j];
        od;
    od;
    return nova_baza;
end;

Print("Določanje vrednosti karakterjev ...\n");
vrednosti_karakterjev := [];;
# za vsako izotipično komponento dobimo en karakter
for i in [1..Length(izotipicne_komponente)] do
    komponenta := izotipicne_komponente[i];;
    # določimo ortogonalno bazo komponente
    baza_komponente := BasisVectors(Basis(komponenta));;
    ortogonalna_baza_komponente := gram_schmidt(baza_komponente);;
    # za vsak predstavnik konjugiranostnega razreda c izračunamo
    # sled preslikave rho(c), zožene na komponento
    # za izračun sledi uporabimo ortogonalno bazo
    vrednosti_karakterjev_te_upodobitve := [];;
    for j in [1..Length(predstavniki_konj_razredov)] do
        c := predstavniki_konj_razredov[j];;
        vrednost_karakterja := Sum(List(ortogonalna_baza_komponente, b -> ComplexConjugate(b) * rho(c) * b / (ComplexConjugate(b) * b))) / Sqrt(Dimension(komponenta));;
        Append(vrednosti_karakterjev_te_upodobitve, [[c, vrednost_karakterja]]);;
    od;
    Append(vrednosti_karakterjev, [vrednosti_karakterjev_te_upodobitve]);;
od;