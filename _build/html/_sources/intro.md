```{raw} html
<div class="naslov">
```

# Teorija upodobitev

```{raw} html
  <strong>Urban Jezernik<br>
  Univerza v Ljubljani, Fakulteta za matematiko in fiziko</strong><br>

  Zadnja posodobitev: 05. 11. 2025
</div>
```

### Kratek opis vsebine

Teorija upodobitev se ukvarja z *linearizacijo* abstraktnih objektov, predvsem grup in njihovih delovanj. Gre za klasično in dobro raziskano vejo matematike, ki ima številne uporabe tudi v drugih znanostih. Dva pomembna cilja, ki ju ta teorija doseže, sta naslednja.

1.  Namesto abstraktne obravnave dano grupo na različne načine uresničimo z obrnljivimi matrikami, kar nam z močnimi orodji linearne algebre omogoča bolj transparenten študij njihovih lastnosti. Tukaj nas zanimajo predvsem najenostavnejši načini predstavitev grup z matrikami.

    <div class="zgledbrezstevilke">

    Opazujmo diedrsko grupo $D_{2n} = \langle s, r \rangle$, v kateri je $s^2 = 1$, $r^n = 1$ in $s r s = r^{-1}$. Ta abstraktna grupa izhaja iz simetrij $n$-kotnika v ravnini, s čimer lahko uresničimo njena generatorja $s,r$ kot matriki
    ```{math}
    s \mapsto \begin{pmatrix}
                    0 & 1 \\ 1 & 0
                \end{pmatrix}, \quad
                r \mapsto \begin{pmatrix}
                    \cos(2 \pi/n) & - \sin(2 \pi/n) \\
                    \sin(2 \pi/n) & \cos(2 \pi/n)
                \end{pmatrix}
    ```
    in torej poljuben element $D_{2n}$ kot matriko v $\GL_2(\RR)$.

    </div>

2.  Mnoge situacije, kjer se pojavljajo grupe prek svojih delovanj, lahko lineariziramo in to linearno strukturo razstavimo na enostavne komponente, ki jih razumemo s pomočjo prejšnje točke.

    <div class="zgledbrezstevilke">

    Opazujmo simetrično grupo $S_n$, ki naravno deluje na množici $\{ 1, 2, \dots, n \}$ s permutacijami. Temu delovanju lahko priredimo vektorski prostor z bazo $\{ e_1, e_2, \dots, e_n \}$. Permutaciji $\sigma \in S_n$ lahko v tej bazi priredimo permutacijsko matriko v $\GL_n(\CC)$, ki vektor $e_i$ preslika v $e_{\sigma(i)}$. Na ta način lahko uresničimo naravno delovanje simetrične grupe $S_n$ znotraj matrične grupe $\GL_n(\CC)$.

    </div>

Najprej bomo vzpostavili temelje teorije upodobitev (osnovne definicije in zgledi, fundamentalne konstrukcije upodobitev). Pokazali bomo, kako se lahko vsaki konkretni upodobitvi približamo, kot da bi jo pogledali pod mikroskopom (videli bomo, da je vsaka sestavljena iz *celic*, vsaka celica pa iz *organelov*). Za tem si bomo ogledali dobro razvito teorijo upodobitev končnih grup (tu bomo pod mikroskopom videli in razumeli čudovito strukturo s pomočjo Fourierove transformacije), podrobneje bomo raziskali upodobitve dveh temeljnih družin končnih grup (simetrične grupe in splošne linearne grupe nad končnim poljem). Ta teorija ima mnogo uporab, od katerih bomo izpostavili nekaj sodobnejših (v teoriji števil, kombinatoriki, slučajnih procesih na grupah). Nazadnje bomo obravnavali še nekaj zgledov upodobitev pomembnih družin neskončnih grup (kompaktne grupe ter linearne grupe, zvezne in diskretne).

### Literatura

Pri predstavitvi temeljev teorije upodobitev uporabljamo jezik homomorfizmov grup (in ne modulov), tako da porabimo več časa za osnove, a je snov predstavljena bolj konkretno. To pride prav predvsem pri razstavljanju dane upodobitve na nerazcepne podupodobitve, kjer sledimo pristopu Kowalskega in opazujemo matrične koeficiente. Karakterje obdelamo v jeziku nekomutativne Fourierove transformacije kot Diaconis. S tem tudi pripravimo teren za kasnejše uporabe teorije upodobitev. Omenimo kolobar virtualnih karakterjev in kot Serre dokažemo Artinov izrek. Razširjena zgleda upodobitev simetričnih grup in splošnih linearnih grup nad končnim poljem pretežno izvedemo s pomočjo monografije Fultona in Harrisa. Pri upodobitvah simetrične grupe določene aspekte izrazimo s Fourierovo transformacijo, pri linearnih grupah pa sledeč Bushnell in Henniart nekoliko bolj naravno predstavimo ostne upodobitve. V uporabah teorije upodobitev predstavimo Rothov izrek po Gowersovo in raziščemo soroden problem za nekomutativne grupe, kjer analitične argumente napravimo kot Eberhard. Pri prepoznavanju komutatorjev nam prav pridejo razvita Fourierova orodja, slučajne sprehode pa raziščemo podobno kot Diaconis. Kompaktne grupe in povezavo s klasično Fourierovo analizo črpamo iz Kowalskega, upodobitve Liejevih grup pa prikažemo kot Fulton in Harris, pri čemer se za integriranje Liejevih homomorfizmov naslonimo na Hallovo knjigo. Diskretne grupe obdelamo sledeč Conradu in Putmanu, razliko med klasičnimi in $p$-adičnimi Liejevimi grupami prikažemo kot Choiy.

- E. Kowalski, *[An Introduction to the Representation Theory of Groups](https://people.math.ethz.ch/~kowalski/representation-theory.pdf)*, American Mathematical Society, 2014.

- P. Diaconis, *Group representations in probability and statistics*, Lecture notes - monograph series 11, i-192, 1988.

- J. P. Serre, *Linear Representations of Finite Groups*, Springer GTM 42, 1977.

- W. Fulton, J. Harris, *Representation Theory: A First Course*, Springer GTM 129, 2004.

- C. J. Bushnell, G. Henniart, *The Local Langlands Conjecture for $\GL(2)$*, Springer Grundlehren der mathematischen Wissenschaften **335**, 2006.

- W. T. Gowers, *[Generalizations of Fourier analysis, and how to apply them](https://arxiv.org/abs/1608.04127)*, Bulletin of the American Mathematical Society **54**, 1-44 (2017).

- S. Eberhard, *[Product mixing in the alternating group](https://arxiv.org/abs/1512.03517)*, Discrete Analysis, 2-18 (2016).

- B. C. Hall, *Lie groups, Lie algebras, and representations*, Quantum Theory for Mathematicians, Springer, New York, NY, 2013.

- K. Conrad, *[$\SL_2(\ZZ)$](https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf)*.

- A. Putman, *[The representation theory of $\SL_n(\ZZ)$](https://www3.nd.edu/~andyp/notes/RepTheorySLnZ.pdf)*.

- K. Choiy, *[A note on the image of continuous homomorphisms of locally profinite groups](https://www.math.purdue.edu/~tongliu/teaching/598/p-adicrep.pdf)*.

### Oblika zapiskov

Zapiski so pripravljeni predvsem v [elektronski obliki](https://urbanjezernik.github.io/teorija-upodobitev/), ki omogoča neposreden dostop do povezanih virov in kratkih kvizov za hitro ponavljanje po poglavjih. Za tiste, ki so raje odklopljeni ali želijo tiskano različico, je na voljo tudi [PDF](https://github.com/urbanjezernik/teorija-upodobitev/blob/main/upodobitve.pdf).

### Zahvala

Zapiske sem v največji meri pripravil med izvajanjem predmeta na magistrskem študiju matematike na Fakulteti za matematiko in fiziko Univerze v Ljubljani v letu 2022/23. Zahvaljujem se študentom, ki so obiskovali predavanja in med spremljanjem opozarjali na vsebinske pomanjkljivosti. Zapiske sta še posebej podrobno pregledala študenta Hana Ibrahimpašić in Daniel Vitas. Zahvaljujem se jima za mnoge koristne pripombe. Za Založbo FMF je zapiske strokovno pregledal Primož Moravec. Njegovi predlogi so naredili delo bolj dostopno študentom, za kar sem mu, kot mu bodo tudi bralci, hvaležen.

```{raw} html
<script defer>
  document.addEventListener('DOMContentLoaded', () => {
    if (!/intro\.html$/.test(window.location.pathname)) return;
    document
      .querySelectorAll('a.headerlink[href="#teorija-upodobitev"][title="Link to this heading"]')
      .forEach(el => el.remove());
    document.querySelectorAll('h2').forEach(h2 => {
      const h3 = document.createElement('h3');
      Array.from(h2.attributes).forEach(({name, value}) =>
        h3.setAttribute(name, value)
      );
      h3.innerHTML = h2.innerHTML;
      h2.replaceWith(h3);
    });
  });
</script>
```
