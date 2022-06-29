g := SymmetricGroup(3);
elementi := Elements(g);
v := FullRowSpace( Rationals, Size(g) );
std_basis := BasisVectors(Basis(v));

rho := function (x)
    local mat, i, y, image_of_y;
    mat := [];
    for i in [1..Size(g)] do
        y := elementi[i];
        image_of_y := std_basis[Position(elementi, y * x^(-1))];
        Append(mat, [image_of_y]);
    od;
    mat := TransposedMat(mat);
    return mat;
end;

cc := List(ConjugacyClasses(g), Representative);

fourier := function (c)
    return Sum(List(ConjugacyClass(g,c), x -> rho(x^(-1))));
end;

for c in cc do
    Eigenspaces(fourier(c));
od;