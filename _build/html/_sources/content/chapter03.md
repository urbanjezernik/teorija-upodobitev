```{raw} html
<style>
  body { counter-reset: chapter 2 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Upodobitve končnih grup

V tem poglavju bomo raziskali kategorijo upodobitev končne grupe s posebnim poudarkom na situaciji, ko je karakteristika polja tuja moči grupe. V tem primeru je, kot bomo videli, vsaka upodobitev polenostavna, zato lahko vprežemo karakterje za razumevanje kategorije upodobitev.

## Polenostavnost

### Nerazcepne upodobitve

Prepričajmo se najprej, da končne grupe nimajo *prevelikih* nerazcepnih upodobitev.

<div class="trditev">

Vsaka nerazcepna upodobitev končne grupe je končno razsežna.

</div>

<div class="dokaz">

Naj bo $G$ končna grupa z upodobitvijo $\rho$ na prostoru $V$. Izberimo poljuben neničeln vektor $v \in V$. Opazujmo podprostor
```{math}
W = \langle \rho(g) \cdot v \mid g \in G \rangle
```
prostora $V$. Ker je $G$ končna, je $W$ končno razsežen. Hkrati je po konstrukciji ta podprostor $G$-invarianten. Vsaka upodobitev končne grupe ima torej končno razsežno podupodobitev. V posebnem to pomeni, da ni neskončno razsežne nerazcepne upodobitve.

</div>

Iz trditve in razmislekov v prejšnjem poglavju sledi, da je vsaka nerazcepna upodobitev končne grupe vsebovana v regularni upodobitvi. Nad algebraično zaprtim poljem dodatno velja, da je razsežnosti kvečjemu $\sqrt{|G|}$.

### Maschkejev izrek

Spoznali smo že, da niso vse upodobitve polenostavne, niti kadar je grupa končna. Videli smo primer grupe $S_3$ z dvorazsežno upodobitvijo $\rho$, ki je bila definirana nad kolobarjem $\ZZ$ in katere projekcija po modulu $3$ *ni* bila polenostavna. Naslednji izrek razkrije, da je to mogoče le v primeru, ko karakteristika polja deli moč grupe.

<div class="izrek">

Naj bo $G$ končna grupa in $F$ polje. Tedaj je vsaka upodobitev $G$ nad poljem $F$ polenostavna, če in samo če $\characteristic(F) \nmid |G|$.

</div>

Preden dokažemo izrek, pojasnimo, kako in zakaj nam prideta prav končnost grupe $G$ in ustrezna karakteristika polja $F$. Ti dve predpostavki namreč odpirata vrata orodju <span class="definicija">povprečenja po grupi</span>. Za dano funkcijo $f \in \fun(G,F)$ lahko v tej ugodni situaciji izračunamo njeno povprečno vrednost[^1]
```{math}
\EE(f) = \frac{1}{|G|} \sum_{g \in G} f(g) \in F.
```
Te račune povprečij lahko razširimo na izračun povprečne linearne preslikave upodobitve. Za dano upodobitev $\rho$ grupe $G$ na prostoru $V$ lahko v tej ugodni situaciji izračunamo njeno povprečno vrednost
```{math}
\EE(\rho) = \frac{1}{|G|} \sum_{g \in G} \rho(g) \in \hom(V,V).
```

<div class="domacanaloga">

Preveri, da je $\EE(\rho) \in \hom_G(V,V)$ projekcijska spletična na podprostor fiksnih vektorjev $V^G$.

</div>

<div class="dokaz">

(dokaz Maschkejevega izreka)

$(\Leftarrow):$ Predpostavimo $\characteristic(F) \nmid |G|$. Naj bo $\rho$ upodobitev grupe $G$ na prostoru $V$ in naj bo $W$ poljuben $G$-invarianten podprostor. Naj bo $P \in \hom(V,V)$ projektor na $W$. Grupa $G$ deluje na prostoru linearnih preslikav $\hom(V,V)$.[^2] Povprečna vrednost tega delovanja je projekcijska spletična na podprostor spletičen $\hom(V,V)^G = \hom_G(V,V)$. Ko to povprečno vrednost uporabimo na projektorju $P$, dobimo torej linearno preslikavo
```{math}
Q = \frac{1}{|G|} \sum_{g \in G} g \cdot P \in \hom_G(V,V),
```
za katero velja $Q|_W = \id_W$ in $\image Q = W$. Torej je $Q$ projekcijska spletična na $W$. Njeno jedro je zato $G$-invarianten komplement prostora $W$ v $V$.

$(\Rightarrow):$ Predpostavimo, da $\characteristic(F) \mid |G|$.[^3] Opazujmo regularno upodobitev $\rho_{\fun}$ na prostoru $\fun(G,F)$. Ta prostor ima vselej $G$-invarianten podprostor
```{math}
\textstyle \fun_0(G,F) = \left\{ f \in \fun(G,F) \mid \sum_{g \in G} f(g) = 0 \right\}
```
korazsežnosti $1$ v $\fun(G,F)$. Dokažimo, da upodobitev na tem podprostoru *ni* komplementirana in da torej vsaka upodobitev ni polenostavna.

Zavoljo protislovja predpostavimo, da komplement obstaja. Imamo torej funkcijo $0 \neq \phi \in \fun(G,F)$, za katero velja $\sum_{g \in G} \phi(g) \neq 0$ in prostor $F \cdot \phi$ je $G$-invarianten. Torej obstaja enorazsežna upodobitev $\chi \colon G \to F^*$, da pri vsakem $g \in G$ velja $g \cdot \phi = \chi(g) \cdot \phi$, se pravi $\phi(g) = \chi(g) \cdot \phi(1)$. Od tod sledi
```{math}
\sum_{g \in G} \phi(g) = \phi(1) \cdot \sum_{g \in G} \chi(g).
```
Trdimo, da je zadnja vsota vselej ničelna, kar nas privede v protislovje s predpostavko $\sum_{g \in G} \phi(g) \neq 0$. Če je namreč $\chi$ trivialna upodobitev, potem iz predpostavke o karakteristiki izpeljemo
```{math}
\sum_{g \in G} \chi(g) = |G| = 0.
```
Če pa $\chi$ ni trivialna, potem za nek $x \in G$ velja $\chi(x) \neq 1$ in v tem primeru izračunamo
```{math}
(\chi(x) - 1) \cdot \sum_{g \in G} \chi(g) = \sum_{g \in G} \chi(xg) - \sum_{g \in G} \chi(g) = 0,
```
kar zopet implicira $\sum_{g \in G} \chi(g) = 0$.

</div>

<div class="zgled">

V ekstremni situaciji, ko je $\characteristic(F) = p > 0$ in $|G| = p^n$ za nek $n \in \NN$, kategorija upodobitev izgleda precej nenavadno. V takih neugodnih razmerah *netrivialnih nerazcepnih upodobitev ni*. Poglejmo si, zakaj je temu tako v primeru $F = \FF_p$ za neko praštevilo $p$.

Imejmo nerazcepno upodobitev $p$-grupe $G$ na prostoru $V$ nad poljem $\FF_p$. Vemo že, da je $V$ nujno končno razsežen, zato je $|V| = p^k$ za nek $k \in \NN$. Grupa $G$ permutacijsko deluje na množici neničelnih vektorjev $V \backslash \{ 0 \}$. Po lemi o orbiti in stabilizatorju je velikost orbite vsakega neničelnega vektorja enaka indeksu stabilizatorja, ki je po predpostavki o moči grupe nujno potenca praštevila $p$. Ker pa moč $|V \backslash \{ 0 \}|$ ni deljiva s $p$, mora obstajati vektor $0 \neq v \in V$ z orbito moči $1$. Ta vektor je torej fiksen za delovanje grupe $G$ in zato razpenja enorazsežen podprostor $\FF_p \cdot v$, ki je kot upodobitev izomorfen $\oneone$. Torej je $V = \oneone$ in upodobitev je res trivialna.

</div>

### Dekompozicija regularne upodobitve

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Vsaka nerazcepna upodobitev $\pi$ grupe $G$ nad $F$ je uresničljiva kot podupodobitev regularne $\rho_{\fun}$. Slednja je po Maschkejevem izreku polenostavna, zato jo lahko zapišemo kot direktno vsoto izotipičnih komponent nerazcepnih upodobitev. Vsaka $\pi$-komponenta pri tem sestoji iz $\deg(\pi)$ mnogo kopij upodobitve $\pi$. Izpostavimo in povzemimo.

<div class="izrek">

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Velja
```{math}
\rho_{\fun} \cong \bigoplus_{\pi \in \Irr(G)} \underbrace{\pi \oplus \pi \oplus \cdots \oplus \pi}_{\deg(\pi)}.
```

</div>

V posebnem iz izreka po primerjavi razsežnosti izpeljemo
```{math}
\sum_{\pi \in \Irr(G)} \deg(\pi)^2 = |G|.
```

<div class="zgled">

- Opazujmo permutacijsko upodobitev $\pi$ grupe $\ZZ/n\ZZ$ na prostoru $\CC[\Omega]$, kjer je $\Omega = \{ 1, 2, \dots, n \}$. Premislili smo že, da je $\pi$ izomorfna regularni upodobitvi in da jo lahko razstavimo kot direktno vsoto $\pi = \bigoplus_{j \in \Omega} \chi_j$, kjer je $\chi_j \colon \ZZ/n\ZZ \to \CC^*$, $x \mapsto e^{2 \pi i j x / n}$, enorazsežna upodobitev. V posebnem od tod sledi, da so $\{ \chi_j \mid j \in \Omega \}$ *vse* neizomorfne nerazcepne upodobitve ciklične grupe $\ZZ/n\ZZ$.

- Naj bo $A$ poljubna končna abelova grupa. Strukturni izrek o abelovih grupah nam pove, da $A$ lahko zapišemo kot direktni produkt določenih cikličnih grup, se pravi $A = C_1 \times C_2 \times \cdots \times C_k$. Kategorijo upodobitev vsake od cikličnih kosov nad $\CC$ že poznamo. Naj bodo $\{ \chi^i_j \mid j \in \Omega_i \}$ nerazcepne upodobitve grupe $C_i$. Tvorimo lahko <span class="definicija">produkt upodobitev</span>
  ```{math}
  \chi^1_{j_1} \times \chi^2_{j_2} \times \cdots \times \chi^k_{j_k} \colon \prod_{i=1}^k C_i = A \to \CC^*, \quad
          (c_1, c_2, \dots, c_k) \mapsto \prod_{i = 1}^k \chi^i_{j_i}(c_i).
  ```
  Na ta način dobimo $\prod_{i=1}^k |\Omega_i| = \prod_{i=1}^k |C_i| = |A|$ enorazsežnih upodobitev. Vsaki dve od teh sta različni med sabo. Na ta način smo torej našli *vse* nerazcepne upodobitve abelove grupe $A$.

</div>

<div class="domacanaloga">

Naj bosta $G_1, G_2$ grupi z nerazcepnima končno razsežnima upodobitvama $\rho_1, \rho_2$ nad algebraično zaprtim poljem. Tedaj je produkt $\rho_1 \times \rho_2$ nerazcepna upodobitev grupe $G_1 \times G_2$. Premisli, da velja tudi obratno; vsaka končno razsežna kompleksna nerazcepna upodobitev grupe $G_1 \times G_2$ je oblike $\rho_1 \times \rho_2$ za neki nerazcepni upodobitvi $\rho_1, \rho_2$.

</div>

### Ortogonalnost matričnih koeficientov

Na prostor funkcij $\fun(G,F)$ uvedimo <span class="definicija">skalarni produkt</span> s predpisom
```{math}
[ f_1, f_2 ] = \frac{1}{|G|} \sum_{g \in G} f_1(g) f_2(g^{-1})
```
za $f_1, f_2 \in \fun(G,F)$. Ker je polje $F$ v splošnem abstraktno, to sicer ni običajen skalarni produkt, je pa to vendarle nedegenerirana simetrična bilinearna forma na $\fun(G,F)$, zato zanjo uporabljamo vso standardno terminologijo iz običajnih skalarnih produktov.

Z uporabo povprečenja na prostoru linearnih preslikav (podobno kot pri dokazu Maschkejevega izreka) bomo nadgradili dekompozicijo regularne upodobitve na *ortogonalno* direktno vsoto.

<div class="trditev">

Naj bo $G$ končna grupa z neizomorfnima nerazcepnima upodobitvima $\pi_1$, $\pi_2$ nad algebraično zaprtim poljem karakteristike tuje $|G|$. Tedaj sta prostora $\MK(\pi_1)$ in $\MK(\pi_2)$ ortogonalna.

</div>

<div class="dokaz">

Naj upodobitvi $\pi_1$, $\pi_2$ delujeta na prostorih $V_1$, $V_2$. Grupa $G$ deluje na prostoru linearnih preslikav $\hom(V_1, V_2)$. Povprečje tega delovanja je projekcijska spletična na podprostor $\hom(V_1, V_2)^G = \hom_G(V_1, V_2)$, ki je po Schurovi lemi trivialen. Za poljubno linearno preslikavo $A \in \hom(V_1, V_2)$ je torej
```{math}
\frac{1}{|G|} \sum_{g \in G} g \cdot A = 0.
```
Izberimo zdaj posebno preslikavo $A$. Naj bo $\{ e_i \}_i$ baza prostora $V_1$ in $\{ f_j \}_j$ baza prostora $V_2$. Vzemimo
```{math}
A_{i,l} \colon V_1 \to V_2, \quad
    v \mapsto \langle e_i^*, v \rangle f_l.
```
S to izbiro dosežemo enakost
```{math}
0 = \frac{1}{|G|} \sum_{g \in G} (g \cdot A_{i,l})(e_j) =
    \frac{1}{|G|} \sum_{g \in G} \langle e_i^*, g^{-1} \cdot e_j \rangle g \cdot f_l =
    \frac{1}{|G|} \sum_{g \in G} f_{i,j}^{\pi_1}(g^{-1}) g \cdot f_l.
```
Na zadnjem uporabimo še $f_k^*$ in dobimo
```{math}
0 = \frac{1}{|G|} \sum_{g \in G} f_{i,j}^{\pi_1}(g^{-1}) \langle f_k^*, g \cdot f_l \rangle =
    \frac{1}{|G|} \sum_{g \in G} f_{i,j}^{\pi_1}(g^{-1}) f_{k,l}^{\pi_2}(g),
```
kar je enakovredno $[ f_{i,j}^{\pi_1}, f_{k,l}^{\pi_2} ] = 0$, se pravi ortogonalnosti matričnih koeficientov.

</div>

Na soroden način lahko analiziramo skalarne produkte znotraj matričnih koeficientov ene same nerazcepne upodobitve.

<div class="trditev">

Naj bo $G$ končna grupa z nerazcepno upodobitvijo $\pi$ nad algebraično zaprtim poljem karakteristike tuje $|G|$. Po izbiri poljubne baze za matrične koeficiente velja
```{math}
[ f_{i,j}, f_{k,l} ] = 
    \begin{cases}
        1/\deg(\pi) & (i,j) = (l,k) \\
        0 & \text{sicer.}
    \end{cases}
```

</div>

<div class="dokaz">

Pristopimo kot pri zadnjem dokazu, pri čemer prostor spletičen $\hom_G(V,V)$ po Schurovi lemi zdaj sestoji le iz skalarnih večkratnikov identitete. Za linearno preslikavo $A \in \hom(V,V)$ je zato
```{math}
\frac{1}{|G|} \sum_{g \in G} g \cdot A = \textstyle \lambda_A \cdot \id_V
```
za nek $\lambda_A \in F$. Velja $g \cdot A = \pi(g) A \pi(g)^{-1}$, zato je $\tr(g \cdot A) = \tr(A)$, od koder izpeljemo
```{math}
\lambda_A = \frac{\tr(A)}{\deg(\pi)}.
```
Kot v zadnjem dokazu dobljeno uporabimo s preslikavo $A_{i,l}(v) = \langle e_i^*, v \rangle e_l$ za neko izbrano bazo $\{ e_i \}_i$ prostora $V$. Velja $\tr(A_{i,l}) = \langle e_i^*, e_l \rangle = 1_{i = l}$, od koder kot v zadnjem dokazu izpeljemo
```{math}
[ f_{i,j}, f_{k,l} ] = \langle e_k^*, e_j \rangle \frac{1_{i = l}}{\deg(\pi)} = \frac{1_{i = l, j = k}}{\deg(\pi)},
```
kar je natanko želeno.

</div>

## Karakterji

Iz rezultatov zadnjega razdelka sledi, da je nad algebraično zaprtim poljem ničelne karakteristike (na primer zelo ugodnim poljem $\CC$) kategorija upodobitev dane končne grupe popolnoma določena z nerazcepnimi upodobitvami, ki jih lahko razumemo s pomočjo karakterjev. V tem razdelku bomo podrobneje razvili to teorijo.

### Ortonormiranost karakterjev

Iz ortogonalnosti matričnih koeficientov z lahkoto izpeljemo ortonormiranost karakterjev.

<div class="posledica">

Naj bo $G$ končna grupa z nerazcepnima upodobitvama $\pi_1$, $\pi_2$ nad algebraično zaprtim poljem karakteristike tuje $|G|$. Velja
```{math}
[ \chi_{\pi_1}, \chi_{\pi_2} ] =
    \begin{cases}
        1 & \pi_1 \cong \pi_2, \\
        0 & \text{sicer.}
    \end{cases}
```

</div>

<div class="dokaz">

Izberemo bazo, izrazimo $\chi_{\pi} = \sum_i f_{i,i}^{\pi}$ in uporabimo zadnji dve trditvi o skalarnih produktih matričnih koeficientov.

</div>

V skladu z običajno terminologijo za funkcijo $f \in \fun(G,F)$ označimo $||f|| = \sqrt{[ f, f ]}$, to je <span class="definicija">norma</span> funkcije $f$. Nerazcepni karakterji tvorijo ortonormiran sistem vektorjev v $\fun(G,F)$.

### Razredne funkcije

Karakterji niso poljubne funkcije v $\fun(G,F)$, temveč vselej pripadajo prostoru $\fun_{\cl}(G,F)$ razrednih funkcij. Vemo že tudi, da so karakterji nerazcepnih upodobitev tudi linearno neodvisni. S pomočjo ortonormiranosti karakterjev bomo sedaj dokazali, da tvorijo celo *bazo* prostora razrednih funkcij.

<div class="izrek">

Naj bo $G$ grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Tedaj karakterji nerazcepnih upodobitev tvorijo ortonormirano bazo prostora $\fun_{\cl}(G,F)$.

</div>

Zopet bomo za dokaz uporabili metodo povprečenja po grupi, a bomo to povprečenje še *utežili*. Za dano funkcijo $f \in \fun(G,F)$ definiramo njeno <span class="definicija">nekomutativno Fourierovo transformacijo</span> $\hat{f}$ kot funkcijo, ki poljubni upodobitvi $\rho$ grupe $G$ na prostoru $V$ priredi
```{math}
\hat{f}(\rho) = \sum_{g \in G} f(g) \rho(g^{-1}) \in \hom(V,V).
```
Fourierova transformacija funkciji $f$ torej priredi njeno uteženo povprečje poljubne upodobitve vzdolž $f$, pri čemer se zgleduje po skalarnem produktu na prostoru funkcij $\fun(G,F)$. V primeru, ko je $f$ konstantna funkcija $1/|G|$, z njeno Fourierovo transformacijo najdemo običajno povprečno vrednost upodobitve $\EE(\rho)$.

<div class="zgled">

- Naj bo $f$ poljubna periodična funkcija na množici $\ZZ$ s periodo $n > 1$ in vrednostmi v $\CC$. Funkcijo $f$ lahko torej obravnavamo kot funkcijo na ciklični grupi $\ZZ/n\ZZ$. Nerazcepne kompleksne upodobitve slednje grupe so ravno enorazsežne upodobitve $\chi_j(x) = e^{2 \pi i j x / n}$ za $j \in \Omega = \{ 1, 2, \dots, n \}$. Nekomutativna Fourierova transformacija funkcije $f$ v teh upodobitvah je
  ```{math}
  \hat{f}(\chi_j) = \sum_{x \in \ZZ/n\ZZ} f(x) e^{- 2 \pi i j x / n }.
  ```
  Vektorju števil $(f(1), f(2), \dots, f(n)) \in \CC^n$ na ta način priredimo vektor števil $(\hat{f}(\chi_1), \hat{f}(\chi_2), \dots, \hat{f}(\chi_n)) \in \CC^n$. To prirejanje je v numerični matematiki znano pod imenom <span class="definicija">diskretna Fourierova transformacija</span> in je fundamentalno v digitalnem procesiranju signalov.

- Naj bo $f \in \fun(G,F)$ funkcija na $G$ in $\rho_{\fun}$ regularna upodobitev grupe $G$. Vrednost $\hat{f}(\rho_{\fun})$ je linearni endomorfizem prostora funkcij $\fun(G,F)$. Pri tem se karakteristična funkcija $1_x$ za $x \in G$ preslika v
  ```{math}
  \hat{f}(\rho_{\fun}) \cdot 1_x 
      = \sum_{g \in G} f(g) \rho_{\fun}(g^{-1}) \cdot 1_x
      = \sum_{g \in G} f(g) 1_{xg}
      = \sum_{g \in G} f(x^{-1}g) 1_{g}.
  ```
  V posebnem pri $x = 1$ dobimo $\hat{f}(\rho_{\fun}) \cdot 1_1 = f$. Funkcijo $f$ lahko torej rekonstruiramo iz vrednosti njene Fourierove transformacije v regularni upodobitvi.

  Regularna upodobitev končne grupe nad ugodnim poljem je direktna vsota nerazcepnih upodobitev grupe, zato je tudi Fourierova transformacija v regularni upodobitvi direktna vsota Fourierovih transformacij v nerazcepnih upodobitvah. Iz zgornjega premisleka sledi, da je vsaka funkcija zatorej enolično določena z vrednostmi svoje Fourierove transformacije v vseh nerazcepnih upodobitvah.

</div>

<div class="lema">

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Za vsako *razredno* funkcijo $f$ in nerazcepno upodobitev $\pi$ na prostoru $V$ je
```{math}
\hat{f}(\pi) = 
    \frac{|G|}{\deg(\pi)} \cdot [ f, \chi_{\pi} ] \cdot {\textstyle \id_V}.
```

</div>

<div class="dokaz">

Za vsak $h \in G$ velja
```{math}
\hat{f}(\pi) \cdot \pi(h) =  \sum_{g \in G} f(g) \pi(g^{-1}h)
    =  \sum_{g \in G} f(g) \pi(h) \pi(h^{-1}g^{-1}h).
```
Izpostavimo $\pi(h)$ in na grupi $G$ uporabimo avtomorfizem $g \mapsto h g h^{-1}$, pa lahko zadnjo vsoto zapišemo kot
```{math}
\pi(h)  \sum_{g \in G} f(hgh^{-1}) \pi(g^{-1}).
```
Ker je $f$ razredna funkcija, je dobljeno ravno enako $\pi(h) \cdot \hat{f}(\pi)$. Vrednost Fourierove transformacije v $\pi$ je torej spletična v $\hom_G(\pi, \pi)$. Po Schurovi lemi sklepamo, da je $\hat{f}(\pi)$ skalarni večkratnik identitete. Njegova sled je enaka
```{math}
\tr \left( \hat{f}(\pi) \right) =  \sum_{g \in G} f(g) \chi_{\pi}(g^{-1}) = |G| \cdot [ f, \chi_{\pi} ].
```
Od tod izračunamo relevantni skalar kot $|G| \cdot [ f, \chi_{\pi} ]/\deg(\pi)$.

</div>

Opremljeni lahko z lahkoto izpeljemo izrek.

<div class="dokaz">

(dokaz izreka o bazi razrednih funkcij)

Predpostavimo, da nerazcepni karakterji *ne* razpenjajo prostora razrednih funkcij. Torej obstaja funkcija $f \in \fun_{\cl}(G,F)$, ki je vsebovana v ortogonalnem komplementu vseh nerazcepnih karakterjev. Za vsak $\pi \in \Irr(G)$ velja torej $[ f, \chi_{\pi} ] = 0$. Preslikava $\hat{f}(\pi)$ je po lemi zato ničelna. Ker to velja za vsako nerazcepno upodobitev, mora veljati tudi za regularno upodobitev, se pravi $\hat{f}(\rho_{\fun}) = 0$. Po zadnjem zgledu to implicira $f = 0$.

</div>

Vsaka razredna funkcija je enolično določena s svojimi vrednostmi v predstavnikih konjugiranostnih razredov. Če <span class="definicija">število konjugiranostnih razredov</span> označimo s $\kk(G)$, velja torej $\dim \fun_{\cl}(G,F) = \kk(G)$. Ker karakterji tvorijo bazo prostora razrednih funkcij, lahko *število* nerazcepnih upodobitev torej izračunamo neposredno iz algebraične strukture grupe.

<div class="posledica">

Za končno grupo $G$ nad algebraično zaprtim poljem karakteristike tuje $|G|$ velja $|\Irr(G)| = \kk(G)$.

</div>

V splošnem *ne* poznamo eksplicitne korespondence[^4] med konjugiranostnimi razredi in nerazcepnimi upodobitvami. Vemo le, da njuni števili sovpadata.

<div class="zgled">

- Opazujmo diedrsko grupo $D_{2n}$ nad poljem $\CC$. Vsak element te grupe lahko zapišemo v obliki $r^i$ ali $s r^i$ za nek $0 \leq i < n$. Izračunajmo konjugiranostne razrede. Velja
  ```{math}
  \left( r^i \right)^{r^j} = r^i, \quad
      \left( r^i \right)^{s r^j} = r^{-i},
  ```
  zato je konjugiranostni razred $r^i$ enak $\{ r^{i}, r^{-i} \}$. Za $i \neq 0, n/2$ ima vsak razred $2$ elementa. Vseh teh konjugiranostnih razredov je torej $\lfloor (n+2)/2 \rfloor$. Velja tudi
  ```{math}
  \left( s r^i \right)^{r^j} = s r^{2j + i}, \quad
      \left( s r^i \right)^{s r^j} = s r^{2j - i},
  ```
  zato je konjugiranostni razred $s$ enak $\{ s r^{2j} \mid j \in \ZZ \}$ in konjugiranostni razred $sr$ je enak $\{ s r^{2j + 1} \mid j \in \ZZ \}$. Če je $n$ sod, sta ta dva razreda disjunktna, če je $n$ lih, pa sovpadata. Skupaj torej dobimo
  ```{math}
  \kk(D_{2n}) = \begin{cases}
          n/2 + 3 & n \equiv 0 \pmod{2}, \\
          (n+3)/2 & n \equiv 1 \pmod{2}. \\
      \end{cases}
  ```

  Določimo zdaj še nerazcepne upodobitve. Poznamo že dvorazsežne nerazcepne upodobitve $\rho_k$ za $0 < k < n/2$, vseh teh je $\lceil n/2 \rceil - 1$. Za karakter take upodobitve velja $\chi_{\rho_k}(r) = 2 \cos(2 \pi k / n)$, zato so vsi ti karakterji različni med sabo in s tem so upodobitve $\rho_k$ neizomorfne. Poleg teh dvorazsežnih upodobitev imamo še linearne upodobitve. Število teh je enako velikosti abelacije $D_{2n}/[D_{2n}, D_{2n}]$.[^5] Velja
  ```{math}
  [r^i, s r^j] = r^{-i} \left( r^i \right)^{s r^j} = r^{-2i}, \quad
      [s r^i, s r^j] = r^{-i} s \left( s r^i \right)^{s r^j} = r^{2j - 2i},
  ```
  zato je $[D_{2n}, D_{2n}] = \langle r^2 \rangle$. S tem je
  ```{math}
  D_{2n}/[D_{2n}, D_{2n}] \cong \begin{cases}
          (\ZZ/2\ZZ)^2 & n \equiv 0 \pmod{2}, \\
          \ZZ/2\ZZ & n \equiv 1 \pmod{2}.
      \end{cases}
  ```
  Linearne upodobitve so torej oblike
  ```{math}
  \chi_{\epsilon, \delta} \colon D_{2n} \to \CC^*, \quad
      s \mapsto \epsilon, \quad
      r \mapsto \delta
  ```
  za $\epsilon, \delta \in \{ 1, -1 \}$. Ko je $n$ lih, je nujno $\delta = 1$.

  Skupaj smo torej našli ravno $\kk(D_{2n})$ nerazcepnih upodobitev, zato so to *vse* nerazcepne upodobitve grupe $D_{2n}$.

  |                     | $1$ |          $r^i$          |    $s$     |
  |:-------------------:|:-----:|:-------------------------:|:------------:|
  | $\chi_{\epsilon}$ | $1$ |           $1$           | $\epsilon$ |
  |  $\chi_{\rho_k}$  | $2$ | $2 \cos(2 \pi i k / n)$ |    $0$     |

  Tabela karakterjev $D_{2n}$ za lih $n$

  <div class="domacanaloga">

  Izračunaj tabelo kompleksnih karakterjev kvaternionske grupe $Q_8 = \{ \pm 1, \pm i, \pm j, \pm k \}$, v kateri velja $i^2 = j^2 = k^2 = ijk = -1$. Primerjaj jo s tabelo karakterjev grupe $D_8$.

  </div>

- Opazujmo simetrično grupo $S_n$ nad poljem $\CC$. Vsako njeno permutacijo $\sigma \in S_n$ lahko zapišemo kot produkt disjunktnih ciklov.[^6] Recimo, da so dolžine teh ciklov enake $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_{k}$. Seveda velja $\sum_{i = 1}^{k} \lambda_i = n$. Zaporedju $(\lambda_1, \lambda_2, \dots, \lambda_{k})$ pravimo <span class="definicija">ciklični tip</span> permutacije $\sigma$. Kadar so kateri od členov cikličnega tipa enaki, ciklični tip pišemo tudi kot $1^{i_1} 2^{i_2} \cdots n^{i_n}$, kjer je $i_m$ število ciklov dolžine $m$ v $\sigma$.

  <div class="domacanaloga">

  Konjugiranostni razredi v $S_n$ so določeni s cikličnim tipom. Natančneje, če je $(\lambda_1, \lambda_2, \dots, \lambda_{k})$ ciklični tip permutacije $\sigma$, potem konjugiranostni razred $\sigma^{S_n}$ sestoji natanko iz vseh permutacij s tem cikličnim tipom. Ta konjugiranostni razred ponavadi označimo kot $\conclass_{(\lambda_1, \lambda_2, \dots, \lambda_k)}$.

  </div>

  V teoriji števil in kombinatoriki cikličnim tipom rečemo tudi <span class="definicija">razčlenitve</span> števila $n$. Število vseh razčlenitev označimo s $p(n)$. Velja torej $p(n) = \kk(S_n) = |\Irr(S_n)|$. Splošna eksplicitna formula za to število *ne* obstaja, poznamo pa njeno asimptotsko oceno
  ```{math}
  p(n) \sim \frac{1}{4 n \sqrt{3}} e^{\pi \sqrt{\frac{2n}{3}}}
  ```
  za $n \to \infty$ [(Hardy-Ramanujan 1918)](https://academic.oup.com/plms/article-abstract/s2-17/1/75/1536632?redirectedFrom=PDF).

  V konkretnem primeru $n = 3$ velja $p(3) = 3$, namreč $3 = 3 = 2 + 1 = 1 + 1 + 1$. Res smo našli natanko $3$ nerazcepne upodobitve grupe $S_3$. V primeru $n = 4$ pa velja $p(4) = 5$. Temu ustrezajo konjugiranostni razredi identične permutacije $()$ ($4 = 1 + 1 + 1 + 1$), transpozicije $(1 \ 2)$ ($4 = 2 + 1 + 1$), tricikla $(1 \ 2 \ 3)$ ($4 = 3 + 1$), štiricikla $(1 \ 2 \ 3 \ 4)$ ($4 = 4$) in produkta dveh tranzpozicij $(1 \ 2)(3 \ 4)$ ($4 = 2 + 2$). Ti konjugiranostni razredi so zaporedoma velikosti $1$, $6$, $8$, $6$, $3$. Kmalu bomo s tem podatkom določili tabelo karakterjev grupe $S_4$.

</div>

Ker nerazcepni karakterji tvorijo ortonormirano bazo prostora razrednih funkcij, lahko vsako razredno funkcijo $f \in \fun_{\cl}(G,F)$ razvijemo po tej bazi kot
```{math}
f = \sum_{\pi \in \Irr(G)} [ f, \chi_{\pi} ] \chi_{\pi}.
```
Alternativna baza prostora razrednih funkcij sestoji iz karakterističnih funkcij konjugiranostnih razredov v $G$. Razvoj te baze po karakterjih nam podaja še eno relacijo med karakterji, ki je ortogonalna[^7] ortonormiranosti.

<div class="posledica">

Naj bo $G$ končna grupa nad algebraično zaprtim poljem karakteristike tuje $|G|$. Za vsaka elementa $g,h \in G$ velja
```{math}
\sum_{\pi \in \Irr(G)} \chi_{\pi}(g) \chi_{\pi}(h^{-1}) = \begin{cases}
        |G|/|g^G| & g^G = h^G, \\
        0 & \text{sicer.}
    \end{cases}
```

</div>

<div class="dokaz">

Karakteristično funkcijo $1_{h^G}$ razvijemo po nerazcepnih karakterjih kot
```{math}
1_{h^G} = \sum_{\pi \in \Irr(G)} [ 1_{h^G}, \chi_{\pi} ] \chi_{\pi}
    = \sum_{\pi \in \Irr(G)} \frac{|h^G|}{|G|} \chi_{\pi}(h^{-1}) \chi_{\pi}
```
in dobljeno evalviramo v elementu $g$.

</div>

### Razstavljanje upodobitve

S pomočjo ortonormirane baze karakterjev lahko z lahkoto razumemo vsako končno razsežno upodobitev končne grupe nad ugodnim poljem.

<div class="posledica">

Naj bo $G$ končna grupa s končno razsežno upodobitvijo $\rho$ nad algebraično zaprtim poljem karakteristike $0$.

1.  Za vsako nerazcepno upodobitev $\pi$ velja $\mult_{\rho}(\pi) = [ \chi_{\rho}, \chi_{\pi} ]$.

2.  $|| \chi_{\rho} ||^2 = \sum_{\pi \in \Irr(G)} \mult_{\rho}(\pi)^2$.

3.  Upodobitev $\rho$ je nerazcepna, če in samo če $|| \chi_{\rho} || = 1$.

</div>

<div class="dokaz">

Upodobitev $\rho$ je polenostavna, zato lahko njen karakter zapišemo kot
```{math}
\chi_{\rho} = \sum_{\pi \in \Irr(G)} \mult_{\rho}(\pi) \cdot \chi_{\pi}.
```
Skalarno pomnožimo s $\chi_{\pi}$ in uporabimo ortonormiranost, pa dobimo $\mult_{\rho}(\pi) = [ \chi_{\rho}, \chi_{\pi} ]$. Od tod izračunamo
```{math}
||\chi_{\rho}||^2 = [ \chi_{\rho}, \chi_{\rho} ] 
    = \sum_{\pi \in \Irr(G)} \mult_{\rho}(\pi) \cdot [ \chi_{\rho}, \chi_{\pi} ] 
    = \sum_{\pi \in \Irr(G)} \mult_{\rho}(\pi)^2.
```
Nazadnje je $||\chi_{\rho}|| = 1$, če in samo če je za natanko eno nerazcepno upodobitev $\pi$ njena večkratnost v $\rho$ enaka $1$, se pravi če je $\rho$ nerazcepna.

</div>

<div class="zgled">

Opazujmo grupo $S_4$ nad poljem $\CC$. Vemo že, da za predstavnike konjugiranostnih razredov lahko izberemo elemente $1 = ()$, $(1 \ 2)$, $(1 \ 2 \ 3)$, $(1 \ 2 \ 3 \ 4)$ in $(1 \ 2)(3 \ 4)$. S tem je število nerazcepnih upodobitev enako $5$. Določimo jih.

Vemo že, da imamo natanko dve enorazsežni upodobitvi, in sicer $\oneone$ in $\sgn$. Naj bo $\pi$ permutacijska upodobitev na prostoru $\CC[\Omega]$, kjer je $\Omega = \{ 1,2,3,4 \}$. V standardni bazi je vsaka matrika te upodobitve permutacijska, zato je vrednost karakterja $\chi_{\pi}$ v permutaciji $\sigma$ ravno število fiksnih točk $\sigma$. V izbranih predstavnikih konjugiranostnih razredov ima torej $\chi_{\pi}$ vrednosti $4, 2, 1, 0, 0$. Od tod izračunamo normo
```{math}
||\chi_{\pi}||^2 = \frac{1}{4!} \left( 1 \cdot 4^2 + 6 \cdot 2^2 + 8 \cdot 1^2  \right)
    = 2.
```
Upodobitev $\pi$ torej *ni* nerazcepna. Velja
```{math}
[ \chi_{\pi}, \chi_{\oneone} ] = \frac{1}{4!} \left( 1 \cdot 4 + 6 \cdot 2 + 8 \cdot 1 \right) = 1,
```
torej $\pi$ vsebuje $\oneone$ z večkratnostjo $1$, kar je povsem analogno temu, kar smo videli pri grupi $S_3$. Zapišemo lahko torej $\pi = \oneone \oplus \rho$ za neko upodobitev $\rho$. Njen karakter ima vrednosti $3,1,0,-1,-1$ in s tem normo
```{math}
||\chi_{\rho}||^2 = \frac{1}{4!} \left( 1 \cdot 3^2 + 6 \cdot 1^2 + 6 \cdot (-1)^2 + 3 \cdot (-1)^2 \right) = 1,
```
zato je upodobitev $\rho$ nerazcepna.

Zaenkrat imamo tri nerazcepne upodobitve stopenj $1,1,3$. Iščemo torej še dve nerazcepni upodobitvi, katerih vsote kvadratov stopenj so enake $24 - (1^2 + 1^2 + 3^2) = 13$. Stopnji teh dveh neznanih upodobitev sta zato nujno enaki $2$ in $3$. Ker že imamo eno nerazcepno upodobitev stopnje $3$, lahko iz nje pridelamo novo s tenzoriranjem z upodobitvijo stopnje $1$. Dobimo upodobitev $\sgn \otimes \rho$. Njen karakter ima vrednosti $3,-1,0,1,-1$ in s tem normo $1$, zato je upodobitev $\sgn \otimes \rho$ res nerazcepna. Nazadnje nam torej manjka le še ena upodobitev stopnje $2$. Imenujmo jo $\tau$. Čeprav je ne poznamo, lahko iz ortonormiranosti karakterjev določimo njen karakter $\chi_{\tau}$ kot natanko tisto razredno funkcijo, ki je ortogonalna na vse poznane neracepne karakterje in je norme $1$ ter pozitivne stopnje. Na ta način dobimo vrednosti $2,0,-1,0,2$. S tem smo nazadnje določili celotno tabelo karakterjev grupe $S_4$ nad $\CC$.[^8]

|  | $()$ | $(1 \ 2)$ | $(1 \ 2 \ 3)$ | $(1 \ 2 \ 3 \ 4)$ | $(1 \ 2)(3 \ 4)$ |
|:--:|:--:|:--:|:--:|:--:|:--:|
| $\chi_{\oneone}$ | $1$ | $1$ | $1$ | $1$ | $1$ |
| $\chi_{\sgn}$ | $1$ | $-1$ | $1$ | $-1$ | $1$ |
| $\chi_{\tau}$ | $2$ | $0$ | $-1$ | $0$ | $2$ |
| $\chi_{\rho}$ | $3$ | $1$ | $0$ | $-1$ | $-1$ |
| $\chi_{\sgn \otimes \rho}$ | $3$ | $-1$ | $0$ | $1$ | $-1$ |

Tabela karakterjev $S_4$

Upodobitve $\tau$ ni težko eksplicitno določiti. Vemo, da je stopnje $2$. Njena vrednost $\tau((1 \ 2)(3 \ 4))$ je matrika v $\GL_2(\CC)$ reda $2$ s sledjo $2$. Taka matrika je lahko le identiteta. Torej je $\tau$ trivialna v konjugiranostnem razredu elementa $(1 \ 2)(3 \ 4)$ in je zato pravzaprav restrikcija upodobitve kvocientne grupe $S_4$ po edinki, generirani s tem konjugiranostnim razredom. Slednjo kvocientno grupo identificiramo kot $S_3$ prek epimorfizma
```{math}
\psi \colon S_4 \to S_3, \quad
    (1 \ 2) \mapsto (1 \ 2), \
    (1 \ 2 \ 3 \ 4) \mapsto (1 \ 3)
```
z jedrom $\{ (), (1 \ 2)(3 \ 4), (1 \ 3)(2 \ 4), (1 \ 4)(2 \ 3) \}$. Upodobitev $\tau$ torej prepoznamo kot restrikcijo dvorazsežne nerazcepne upodobitve grupe $S_3$ vzdolž homomorfizma $\psi$.

</div>

### Projekcije na izotipične komponente

Dekompozicijo regularne upodobitve smo dobili iz matričnih koeficientov nerazcepnih upodobitev, torej gre za nekakšno *notranjo* dekompozicijo. Obstaja pa tudi *zunanja* dekompozicija, pri kateri iz upodobitve same s pomočjo ustreznih projekcijskih spletičen najdemo izotipične komponente upodobitve.

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Naj bo $\rho$ podupodobitev regularne upodobitve $\rho_{\fun}$ na prostoru $V \leq \fun(G,F)$. Ta prostor lahko predstavimo kot sliko neke projekcijske spletične $\Phi \in \hom_G(\rho_{\fun}, \rho)$. Res je tudi obratno, vsaka spletična $\Phi \in \hom_G(\rho_{\fun}, \rho_{\fun})$ podaja prek svoje slike podupodobitev regularne upodobitve. Podupodobitve so torej parametrizirane s spletičnami. Izkaže se, da te vselej izhajajo iz Fourierovih transformacij.

<div class="trditev">

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Preslikava
```{math}
\Fcal \colon \fun(G,F) \to \hom_G(\rho_{\fun}, \rho_{\fun}), \quad
    f \mapsto \left( h \mapsto \hat{h}(\rho_{\fun}) \cdot f \right)
```
je izomorfizem vektorskih prostorov.

</div>

<div class="dokaz">

Ni težko preveriti, da je $\Fcal$ dobro definirana preslikava. Očitno je linearna. Za $f \in \fun(G,F)$ je $\Fcal(f) \cdot 1_1 = \widehat{1_1}(\rho_{\fun}) \cdot f = f$, zato je $\Fcal$ injektivna. Oba prostora sta enake razsežnosti, namreč $|G|$, zato je $\Fcal$ izomorfizem.

</div>

V posebnem je vsaka endospletična regularne upodobitve enaka evalvaciji Fourierove transformacije v neki fiksni funkciji.[^9] Nekoliko natančneje si poglejmo, kaj je ta evalvacija. Za funkciji $f,h \in \fun(G,F)$ je
```{math}
\hat{h}(\rho_{\fun}) \cdot f = \sum_{g \in G} h(g) \rho_{\fun}(g^{-1}) \cdot f =
    \left( x \mapsto \sum_{g \in G} h(g) f(x g^{-1}) \right).
```
Zadnjo vsoto prepoznamo kot <span class="definicija">konvolucijo</span> funkcij $f$ in $h$, se pravi
```{math}
\left( f * h \right) (x) = \sum_{g \in G} f(x g^{-1}) h(g).
```
Velja torej $\hat{h}(\rho_{\fun}) \cdot f = f * h$. Če dodatno predpostavimo, da je $f$ razredna funkcija, potem se ni težko prepričati, da velja $f * h = h * f$, torej je v tem primeru
```{math}
\Fcal(f) \cdot h = \hat{h}(\rho_{\fun}) \cdot f = \hat{f}(\rho_{\fun}) \cdot h
```
in zato preslikava $\Fcal$ ni nič drugega kot običajna Fourierova transformacija razredne funkcije. V posebnem so torej Fourierove transformacije karakterjev endospletične regularne upodobitve. Izkaže se, da so te vselej tesno povezane s projekcijami na izotipične komponente.

<div class="trditev">

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Za vsako končno razsežno upodobitev $\rho$ in nerazcepno upodobitev $\pi$ je
```{math}
\frac{\deg(\pi)}{|G|} \cdot \widehat{\chi_{\pi}}(\rho)
```
projektor na $\pi$-izotipično komponento v $\rho$.

</div>

<div class="dokaz">

Iz leme o Fourierovi transformaciji razredne funkcije izpeljemo, da za vsaki nerazcepni upodobitvi $\pi_1$, $\pi_2$ na prostorih $V_1$, $V_2$ velja
```{math}
\frac{\deg(\pi_1)}{|G|} \cdot \widehat{\chi_{\pi_1}}(\pi_2) = \begin{cases}
        {\textstyle \id_{V_2}} & \pi_1 \cong \pi_2, \\
        0 & \text{sicer.}
    \end{cases}
```
Ko upodobitev $\rho$ razstavimo na direktno vsoto nerazcepnih podupodobitev, je linearni endomorfizem $\deg(\pi)/|G| \cdot \widehat{\chi_{\pi}}(\rho)$ torej ničeln na podupodobitvah, ki niso izomorfne $\pi$, in identiteta na podupodobitvah, ki so izomorfne $\pi$. Ta endomorfizem je torej projektor na direktno vsoto podupodobitev, ki so izomorfne $\pi$, torej ravno na $\pi$-izotipično komponento.

</div>

<div class="zgled">

Naj bo $\rho_{\fun}$ regularna upodobitev grupe $G$. Vemo že, da za vsako funkcijo $f \in \fun(G,F)$ velja $\hat{f}(\rho_{\fun}) \cdot 1_1 = f$. Torej je projekcija funkcije $1_1$ na $\pi$-izotipično komponento enaka
```{math}
\frac{\deg(\pi)}{|G|} \cdot \widehat{\chi_{\pi}}(\rho_{\fun}) \cdot 1_1 = 
    \frac{\deg(\pi)}{|G|} \cdot \chi_{\pi}.
```
S tem dobimo razvoj
```{math}
1_1 = \frac{1}{|G|} \sum_{\pi \in \Irr(G)} \chi_{\pi}(1) \cdot \chi_{\pi},
```
ki je le poseben primer druge ortogonalnostne relacije.

Oglejmo si še karakteristično funkcijo $1_x$ za $x \in G$. Njena projekcija na $\pi$-izotipično komponento je
```{math}
\frac{\deg(\pi)}{|G|} \cdot \widehat{\chi_{\pi}}(\rho_{\fun}) \cdot 1_x = 
    \frac{\deg(\pi)}{|G|} \cdot \left( g \mapsto \chi_{\pi}(x^{-1}g) \right),
```
s čimer dobimo razvoj
```{math}
1_x(g) = \frac{1}{|G|} \sum_{\pi \in \Irr(G)} \chi_{\pi}(1) \chi_{\pi}(x^{-1} g).
```

</div>

Vsako funkcijo $f \in \fun(G,F)$ lahko razvijemo po karakterističnih funkcijah kot $f = \sum_{x \in G} f(x) 1_x$. Ker že poznamo razvoj vsake od karakterističnih funkcij po $\pi$-izotipičnih komponentah, od tod izpeljemo
```{math}
f(g) = \frac{1}{|G|} \sum_{\pi \in \Irr(G)} \sum_{x \in G} f(x) \chi_{\pi}(1) \tr \left( \pi(x^{-1}) \cdot \pi(g) \right),
```
kar lahko po upoštevanju linearnosti sledi izrazimo kot
```{math}
f(g) = \frac{1}{|G|} \sum_{\pi \in \Irr(G)} \chi_{\pi}(1) \tr \left( \hat{f}(\pi) \cdot \pi(g) \right).
```
Temu razvoju funkcije $f$ po $\pi$-izotipičnih komponentah rečemo <span class="definicija">Fourierova inverzija</span>, saj nam ekplicitno pove, kako lahko $f$ izračunamo iz njenih Fourierovih transformacij v nerazcepnih upodobitvah.

<div class="zgled">

Naj bo $A$ končna abelova grupa. Vemo že, da so vse njene kompleksne nerazcepne upodobitve enorazsežne. V tem primeru so upodobitve kar enake svojim karakterjem. Za dano funkcijo $f \in \fun(A,\CC)$ lahko Fourierovo inverzijo zapišemo kot
```{math}
f = \frac{1}{|A|} \sum_{\chi \in \Irr(A)} \hat{f}(\chi) \cdot \chi,
```
kar je le posledica dejstva $\hat{f}(\chi) = |A| \cdot [ f, \chi ]$.

</div>

### Izračunljivost tabele karakterjev

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Kategorijo $\Rep_G$ v tem primeru razumemo zelo dobro, če le poznamo tabelo karakterjev. Za zdaj smo si pogledali nekaj zgledov, kako to tabelo izračunati za posebne primere grupe. Pri tem smo si sicer res pomagali z razvito teorijo, a je bil večji del izračuna tabele opravljen z metodo ostrega pogleda. V splošnem se temu lahko izognemo; obstaja namreč več algoritmov, ki le z uporabo linearne algebre izračunajo tabelo karakterjev.

Pogledali si bomo enega takih algoritmov, ki uporablja projekcije na izotipične komponente iz zadnjega razdelka. Algoritem temelji na Fourierovi transformaciji karakteristične funkcije $1_{\conclass}$ konjugiranostnega razreda $\conclass$ grupe $G$ v regularni upodobitvi $\rho_{\fun}$. Po lemi o Fourierovi transformaciji razredne funkcije je namreč zožitev $\widehat{1_{\conclass}}(\rho_{\fun})$ na $\pi$-izotipično komponento skalarno množenje s številom
```{math}
\frac{|G|}{\deg(\pi)} \cdot [1_{\conclass}, \chi_{\pi}] =
    |\conclass| \cdot \frac{\chi_{\pi}(\conclass^{-1})}{\chi_{\pi}(1)}.
```
Vektorji v $\pi$-izotipični komponenti so zato hkratni lastni vektorji preslikav $\widehat{1_{\conclass}}(\rho_{\fun})$, ko $\conclass$ preteče vse konjugiranostne razrede grupe $G$. Pokažimo, da je ta opis v resnici karakterizacija $\pi$-izotipičnih komponent.

<div class="lema">

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Izotipične komponente regularne upodobitve so natanko netrivialni preseki lastnih podprostorov $\widehat{1_{\conclass}}(\rho_{\fun})$, ko $\conclass$ preteče vse konjugiranostne razrede grupe $G$.

</div>

<div class="dokaz">

Naj bo
```{math}
\textstyle W = \bigcap_{\conclass} \Eigenspace_{\lambda_{\conclass}}\left(\widehat{1_{\conclass}}(\rho_{\fun})\right) \leq \fun(G,F)
```
presek lastnih podprostorov[^10] za neke skalarje $\lambda_{\conclass}$, kjer presek teče po vseh konjugiranostnih razredih grupe $G$. Predpostavimo, da je $W \neq 0$. Naj bo $w \in W$. Za $\pi \in \Irr(G)$ naj bo $P_{\pi}$ projekcija na $\pi$-izotipično komponento. Velja
```{math}
P_{\pi} \cdot w = \frac{\chi_{\pi}(1)}{|G|} \widehat{\chi_{\pi}}(\rho_{\fun}) \cdot w =
    \frac{\chi_{\pi}(1)}{|G|} \sum_{g \in G} \chi_{\pi}(g) \rho_{\fun}(g^{-1}) \cdot w.
```
Vsoto lahko razvijemo po vsakem konjugiranostnem razredu posebej in dobimo
```{math}
\frac{\chi_{\pi}(1)}{|G|} \sum_{\conclass} \chi_{\pi}(\conclass) \sum_{g \in \conclass} \rho_{\fun}(g^{-1}) \cdot w =
    \left( \frac{\chi_{\pi}(1)}{|G|} \sum_{\conclass} \chi_{\pi}(\conclass) \lambda_{\conclass} \right) w
```
kjer smo v enakosti upoštevali, da je $w \in W$. Od tod sledi
```{math}
\textstyle W \leq \Eigenspace_{\frac{\chi_{\pi}(1)}{|G|} \sum_{\conclass} \chi_{\pi}(\conclass) \lambda_{\conclass}}(P_{\pi}).
```
Projektor $P_{\pi}$ ima seveda le dve možni lastni vrednosti: $0$ in $1$. Ker je po predpostavki $W \neq 0$, ne more biti za vse $\pi \in \Irr(G)$ projekcija na $\pi$-izotipično komponento ničelna na $W$. Torej je za nek $\pi$ nujno
```{math}
\textstyle W \leq \Eigenspace_{1}(P_{\pi}) = \Izotip_{\rho_{\fun}}(\pi).
```
Vemo že, kako deluje $\widehat{1_{\conclass}}(\rho_{\fun})$ na $\pi$-izotipični komponenti, od koder določimo skalarje kot $\lambda_{\conclass} = |\conclass| \cdot \chi_{\pi}(\conclass^{-1})/\chi_{\pi}(1)$. Iz definicije $W$ zdaj sledi, da je $\pi$-izotipična komponenta vsebovana v $W$, s čimer smo nazadnje izpeljali $W = \Izotip_{\rho_{\fun}}(\pi)$.

</div>

S to karakterizacijo izotipičnih komponent lahko opišemo algoritem za izračun tabele karakterjev.[^11] Najprej oštevilčimo elemente grupe $G$ kot $g_1, g_2, \dots, g_{|G|}$ in pripravimo vektorski prostor $F^{|G|} \cong \fun(G,F)$ s standardno bazo $e_i$, ki ustreza karakteristični funkciji $1_{g_i}$. Izračunamo še konjugiranostne razrede grupe $G$ in iz vsakega izberemo predstavnika. Pripravimo funkcijo, ki izračuna matriko regularne upodobitve $\rho_{\fun}$ v poljubnem elementu $x \in G$, in za tem še funkcijo, ki izračuna matriko Fourierove transformacije $\widehat{1_{\conclass}}(\rho_{\fun})$ za konjugiranostni razred $\conclass$. Izračunamo lastne podprostore vseh teh matrik in za tem vse njihove netrivialne preseke. Te so ravno izotipične komponente. V vsaki komponenti $W$ izberemo bazo, v kateri izračunamo sled zožitve matrike $\rho_{\fun}(x)$ na $W$. Ker je $W$ kot upodobitev izomorfen direktni vsoti $\deg(\pi)$ kopij neke nerazcepne upodobitve $\pi$, velja $\dim(W) = \deg(\pi)^2$ in zato
```{math}
\tr(\rho_{\fun}(x) |_W) = \sqrt{\dim(W)} \cdot \chi_{\pi}(x).
```
Iz izračunane sledi torej lahko določimo vrednost pripadajočega karakterja v predstavnikih konjugiranostnih razredov. Implementacija predstavljenega algoritma za izračun tabele karakterjev nad $\CC$ v programskem jeziku GAP[^12] je dostopna [tukaj](https://github.com/urbanjezernik/teorija-upodobitev/blob/main/racunanje-tabele.g).

<div class="zgled">

Opazujmo alternirajočo grupo $A_5$ nad poljem $\CC$. Z opisanim algoritmom hitro izračunamo njeno tabelo karakterjev.

|  | $()$ | $(1 \ 2)(3 \ 4)$ | $(1 \ 2 \ 3)$ | $(1 \ 2 \ 3 \ 4 \ 5)$ | $(1 \ 2 \ 3 \ 5 \ 4)$ |
|:--:|:--:|:--:|:--:|:--:|:--:|
| $\chi_1$ | $1$ | $1$ | $1$ | $1$ | $1$ |
| $\chi_2$ | $5$ | $1$ | $-1$ | $0$ | $0$ |
| $\chi_3$ | $4$ | $0$ | $1$ | $-1$ | $-1$ |
| $\chi_4$ | $3$ | $-1$ | $0$ | $-\zeta^2-\zeta^3$ | $-\zeta-\zeta^4$ |
| $\chi_5$ | $3$ | $-1$ | $0$ | $-\zeta-\zeta^4$ | $-\zeta^2-\zeta^3$ |

Tabela karakterjev $A_5$, kjer je $\zeta = e^{2 \pi i / 5}$

Iz tabele lahko razberemo kar nekaj lastnosti grupe. Poglejmo si, kako hitro premislimo, da je $A_5$ *enostavna* grupa. Če bi namreč $A_5$ imela kakšno pravo netrivialno edinko $N$, potem bi kvocient $A_5/N$ imel kakšno netrivialno nerazcepno upodobitev $\rho$. Restrikcija $\Res^{A_5/N}_{A_5}(\rho)$ je zato netrivialna nerazcepna upodobitev grupe $A_5$ z netrivialnim jedrom. Vrednost karakterja $\chi_{\rho}$ v poljubnem elementu $N$ je torej enaka $\chi_{\rho}(1)$. Iz tabele karakterjev grupe $A_5$ pa je jasno, da takega karakterja ni.[^13]

</div>

Predstavljeni algoritem ima mnogo pomanjkljivosti. V programskem jeziku GAP je za izračun tabele karakterjev implementiran algoritem [(Dixon 1967, Schneider 1990)](https://www.sciencedirect.com/science/article/pii/S0747717108800776), ki izboljša predstavljenega na naslednja dva načina.

1.  S predstavljenim algoritmom bomo težko izračunali tabelo karakterjev kakšne zelo velike grupe, saj moramo v postopku diagonalizirati matrike velikosti $|G| \times |G|$. Algoritem v GAP sicer temelji na enaki ideji iskanja skupnih lastnih podprostorov, a pri tem ne opazuje regularne upodobitve, temveč upošteva abstraktne formule med karakterji in iz njih izpelje matrike velikosti $\kk(G) \times \kk(G)$, katerih skupni lastni vektorji so (bolj ali manj) karakterji. Ker je število $\kk(G)$ bistveno manjše od $|G|$, je ta izračun mnogo lažji in hitrejši.

2.  Za izračun natančnih vrednosti karakterjev moramo vse račune izvajati eksaktno in brez približkov. Numerične metode, ki jih sicer lahko uporabimo za hitro računanje lastnih vrednosti velikih matrik, torej odpadejo. Programski jezik GAP zna računati simbolično, a je to lahko precej zamudno. Algoritem v GAP se temu izogne tako, da večino računov opravi nad poljem $\FF_p$ za ustrezno izbrano dovolj veliko praštevilo $p$, potem pa te rezultate prenese nazaj nad $\CC$. Vsi računi so zato hitri in eksaktni.

### Kolobar virtualnih karakterjev

Pogosto nas ne zanima le računski aspekt upodobitev, temveč konceptualno razumevanje, od kod prihajajo nerazcepne upodobitve dane grupe. Kot bomo videli, tukaj igra glavno vlogo indukcija.

Naj bo $G$ grupa in $F$ polje karakteristike tuje $|G|$. Karakterji upodobitev grupe $G$ so celoštevilske kombinacije nerazcepnih karakterjev. Tvorimo množico vseh takih kombinacij, se pravi
```{math}
R(G) = \bigoplus_{\pi \in \Irr(G)} \ZZ \cdot \chi_{\pi} \subseteq \textstyle \fun_{\cl}(G, F).
```
Množica $R(G)$ je najprej očitno abelova podgrupa razrednih funkcij. Za tem je opremljena z množenjem, ki izhaja iz tenzorskega produkta upodobitev. Množica $R(G)$ na ta način postane komutativen podkolobar v $\fun_{\cl}(G,F)$, ki ga imenujemo <span class="definicija">kolobar virtualnih karakterjev</span>.[^14]

Naj bo $H$ podgrupa v $G$. Restrikcija vzdolž vložitve $H$ v $G$ porodi *homomorfizem kolobarjev*
```{math}
\textstyle \Res \colon R(G) \to R(H), \quad \chi_{\pi} \mapsto \chi_{\Res^G_H(\pi)}.
```
Sorodno dobimo z indukcijo preslikavo
```{math}
\textstyle \Ind \colon R(H) \to R(G), \quad \chi_{\pi} \mapsto \chi_{\Ind^G_H(\pi)},
```
ki pa je le *homomorfizem abelovih grup*. Ob koncu razdelka o indukciji smo za upodobitvi $\rho$ v $\Rep_G$ in $\sigma$ v $\Rep_H$ zapisali izomorfizem
```{math}
\textstyle \Ind^G_H(\Res^G_H(\rho) \otimes \sigma) \cong
        \rho \otimes \Ind^G_H(\sigma),
```
ki ga zdaj lahko interpretiramo s karakterji teh upodobitev in sklenemo, da je slika $\Ind(R(H))$ *ideal* v $R(G)$.

<div class="zgled">

Naj bo $H$ ciklična grupa. Definirajmo indikatorsko funkcijo generatorjev grupe $H$ kot
```{math}
c_H \colon H \to F, \quad
    h \mapsto \begin{cases} |H| & \langle h \rangle = H, \\ 0 & \text{sicer.} \end{cases}
```
Ker je $H$ abelova grupa, je seveda $c_H \in \fun_{\cl}(H,F)$.

Premislimo, da velja celo $c_H \in R(H)$. Dokazujmo z indukcijo na $|H|$. Vsaka prava podgrupa $K \leq H$ je tudi ciklična, zato zanjo po indukcijski predpostavki velja $c_K \in R(K)$. Naj bo $R$ množica predstavnikov odsekov $K$ v $H$. S formulo za indukcijo karakterja za $h \in H$ izračunamo
```{math}
{\textstyle \Ind^H_K(c_K)(h)} = \sum_{r \in R \colon h \in K} c_K(h) =
    \begin{cases} |H:K| c_K(h) & h \in K, \\ 0 & \text{sicer}  \end{cases} =
    \begin{cases}  |H| & \langle h \rangle = K, \\ 0 & \text{sicer.} \\ \end{cases}
```
Vsak element $h \in H$ generira neko podgrupo $H$, bodisi pravo bodisi kar $H$. Torej lahko zapišemo
```{math}
c_H = |H| - \sum_{K < H} \textstyle  \Ind^H_K(c_K).
```
Konstanta $|H|$ je karakter trivialne upodobitve $\oneone^{|H|}$ grupe $H$, torej iz zadnje enakosti sledi želeno $c_H \in R(H)$.

</div>

Naj bo $C$ množica vseh cikličnih pogrup grupe $G$ in izberimo $H \in C$. Naj bo $R$ množica predstavnikov desnih odsekov $H$ v $G$. Zadnji zgled nam pove $c_H \in R(H)$. Ta virtualni karakter lahko induciramo na grupo $G$ in za $g \in G$ dobimo
```{math}
{\textstyle \Ind^G_H(c_H)(g)} = \sum_{r \in R \colon r g r^{-1} \in H} c_H(r g r^{-1}) =
    \sum_{r \in R \colon \langle r g r^{-1} \rangle = H} |H| =
    \sum_{x \in G \colon  \langle x g x^{-1} \rangle = H} 1.
```
Ko torej seštejemo prispevke po vseh cikličnih podgrupah, dobimo
```{math}
\sum_{H \in C} {\textstyle \Ind^G_H(c_H)(g)} = \sum_{x \in G} \sum_{H \in C} 1_{\langle x g x^{-1} \rangle = H} = \sum_{x \in G} 1 = |G|.
```
Konstantna funkcija $|G|$ je torej element ideala $\sum_{H \in C} \Ind(R(H))$ v $R(G)$. Od tod seveda sledi vsebovanost
```{math}
|G| \cdot R(G) \leq \sum_{H \in C} \Ind(R(H)).
```
Vsak virtualni karakter v $R(G)$ je zato linearna kombinacija induciranih virtualnih karakterjev cikličnih podgrup, pri čemer so koeficienti racionalna števila z imenovalcem kvečjemu $|G|$. Povzemimo to presenetljivo ugotovitev.

<div class="izrek">

Naj bo $G$ končna grupa in $\rho$ njena končno razsežna upodobitev nad poljem karakteristike tuje $|G|$. Tedaj je $\chi_{\rho}$ *racionalna* linearna kombinacija indukcij nerazcepnih karakterjev cikličnih podgrup grupe $G$.

</div>

Racionalnim kombinacijam se lahko izognemo, če razširimo razred podgrup s cikličnih na <span class="definicija">$p$-elementarne podgrupe</span> grupe $G$. To so podgrupe, ki so izomorfne direktnemu produktu ciklične grupe in $p$-grupe.

<div class="izrek">

Naj bo $G$ končna grupa in $\rho$ njena končno razsežna upodobitev nad algebraično zaprtim poljem karakteristike $0$. Tedaj je $\chi_{\rho}$ *celoštevilska* linearna kombinacija indukcij nerazcepnih karakterjev $p$-elementarnih podgrup grupe $G$, ko $p$ preteče vse praštevilske delitelje moči $G$.

</div>

Dokaz Brauerjevega izreka je nekoliko bolj zapleten kot preprost argument, ki nas je pripeljal do Artinovega izreka. Bralec ga lahko najde v (Serre 1977).

Ne spreglejmo ključne lekcije tega razdelka: nerazcepne upodobitve dane končne grupe iščemo s pomočjo indukcije iz preprostih podgrup.

### Kompleksne upodobitve

Splošno teorijo upodobitev končnih grup zaključimo z upodobitvami nad najugodnejšim poljem $\CC$. To polje je daleč od abstraktnega in je opremljeno z mnogo dodatne strukture, ki jo lahko pri upodobitvah izkoristimo.

#### Vrednosti karakterjev

Najprej si oglejmo nekaj dodatnih lastnosti, ki jih imajo karakterji kompleksnih upodobitev. Njihove vrednosti namreč niso čisto poljubna kompleksna števila, temveč so algebraična cela števila[^15] omejene absolutne vrednosti.

<div class="trditev">

Naj bo $G$ končna grupa. Za vsako končno razsežno kompleksno upodobitev $\rho$ in vsak $g \in G$ je
```{math}
|\chi_{\rho}(g)| \leq \deg(\rho), \quad
    \chi_{\rho}(g) \in \bar{\ZZ}, \quad
    \chi_{\rho}(g^{-1}) = \overline{\chi_{\rho}(g)}.
```

</div>

<div class="dokaz">

Velja $\rho(g^{|G|}) = \rho(1) = \id$, zato je $\rho(g)$ linearna preslikava končnega reda. Take preslikave so diagonalizabilne.[^16] Naj bo $\Eigenvalues(\rho(g)) \subseteq \CC^*$ množica lastnih vrednosti $\rho(g)$. Vsaka lastna vrednost $\lambda \in \Eigenvalues(\rho(g))$ je končnega reda v $\CC^*$. S tem je seveda
```{math}
\chi_{\rho}(g) = \sum_{\lambda \in \Eigenvalues(\rho(g))} \lambda \in \bar{\ZZ},
    \quad
    |\chi_{\rho}(g)| \leq \sum_{\lambda \in \Eigenvalues(\rho(g))} |\lambda| = \deg(\rho)
```
in hkrati
```{math}
\chi_{\rho}(g^{-1}) = \sum_{\lambda \in \Eigenvalues(\rho(g))} \lambda^{-1}
    = \sum_{\lambda \in \Eigenvalues(\rho(g))} \overline{\lambda}
    = \overline{\chi_{\rho}(g)}.
```

</div>

S pomočjo te restriktivne lastnosti vrednosti karakterjev lahko izpeljemo pomembno lastnost stopenj nerazcepnih kompleksnih upodobitev.

<div class="izrek">

Stopnja vsake nerazcepne kompleksne upodobitve končne grupe deli moč grupe.

</div>

Dokaz bomo navezali na edino mesto, kjer smo že videli ulomek $|G|/\deg(\pi)$, in sicer je to lema o Fourierovi transformaciji razredne funkcije. Ko funkcija, vzdolž katere izvedemo transformacijo, slika v kolobar algebraičnih celih števil, lahko lemo o Fourierovi transformaciji razredne funkcije zaostrimo na naslednji način.

<div class="lema">

Naj bo $G$ končna grupa. Za vsako funkcijo $f \in \fun_{\cl}(G, \bar{\ZZ})$ in nerazcepno kompleksno upodobitev $\pi$ je $\hat{f}(\pi)$ skalarno množenje z algebraičnim celim številom.

</div>

<div class="dokaz">

Vemo že, da je $\hat{f}(\pi)$ skalarno množenje s številom
```{math}
\frac{|G|}{\deg(\pi)} \cdot [ f, \chi_{\pi} ].
```
Preveriti moramo torej, da je to algebraično celo število. Funkcijo $f$ lahko razvijemo kot vsoto karakterističnih funkcij konjugiranostnih razredov s koeficienti v $\bar{\ZZ}$. Ker $\bar{\ZZ}$ tvori kolobar, bo torej trditev dovolj preveriti za primer, ko je $f = 1_{\conclass}$ za nek konjugiranostni razred $\conclass$ v $G$.

Vse nerazcepne upodobitve lahko obravnavamo v enem zamahu, in sicer tako, da opazujemo regularno upodobitev in s tem linearno preslikavo $\widehat{1_{\conclass}}(\rho_{\fun})$. Na vsaki od podupodobitev, ki je izomorfna $\pi$, ta preslikava deluje kot $\widehat{1_{\conclass}}(\pi)$, torej kot skalarno množenje z gornjim številom. To število je zato lastna vrednost preslikave $\widehat{1_{\conclass}}(\rho_{\fun})$.

Vemo že, da $\widehat{1_{\conclass}}(\rho_{\fun})$ deluje na naravni bazi iz karakterističnih funkcij $1_x$ za $x \in G$ kot
```{math}
\widehat{1_{\conclass}}(\rho_{\fun}) \cdot 1_x = \sum_{g \in G} 1_{\conclass}(x^{-1} g) 1_g \in \fun(G, \{ 0, 1 \}).
```
V tej bazi ima torej $\widehat{1_{\conclass}}(\rho_{\fun})$ matriko s koeficienti v množici $\{ 0, 1 \}$. Karakteristični polinom te matrike ima zato celoštevilske koeficiente, torej so lastne vrednosti preslikave $\widehat{1_{\conclass}}(\rho_{\fun})$ algebraična cela števila.

</div>

<div class="dokaz">

(dokaz izreka o stopnjah upodobitev)

Naj bo $\pi \in \Irr(G)$. Uporabimo lemo s funkcijo $f = \chi_{\pi}$, ki nam pove, da je
```{math}
\frac{|G|}{\deg(\pi)} \cdot [ \chi_{\pi}, \chi_{\pi} ] = \frac{|G|}{\deg(\pi)} \in \bar{\ZZ}.
```
Ker je zadnje število hkrati v $\QQ$, je torej v $\QQ \cap \bar{\ZZ} = \ZZ$.

</div>

#### Skalarni produkti in unitarnost

Polje $\CC$ je opremljeno s standardnim skalarnim produktom $\langle z, w \rangle = z \cdot \overline{w}$. Ta produkt lahko razširimo na vsak končno razsežen kompleksen vektorski prostor. Obravnavali bomo dve taki razširitvi, in sicer na prostor funkcij $\fun(G,\CC)$ ter na vektorski prostor, na katerem upodabljamo grupo $G$.

Opazujmo najprej prostor funkcij $\fun(G,\CC)$. Vemo že, da ga lahko opremimo s skalarnim produktom $[\cdot, \cdot]$. Ker pa je ta prostor kompleksen, lahko nanj vpeljemo še <span class="definicija">standarden kompleksni skalarni produkt</span>,
```{math}
\langle f, h \rangle = \frac{1}{|G|} \sum_{g \in G} f(g) \overline{h(g)}
```
za $f,h \in \fun(G,\CC)$. Za vsako končno razsežno kompleksno upodobitev $\rho$ po zadnji trditvi velja
```{math}
[f, \chi_{\rho}] = \langle f, \chi_{\rho} \rangle,
```
zato se večina rezultatov, ki smo jih izpeljali za skalarni produkt $[\cdot, \cdot]$, prenese na skalarni produkt $\langle \cdot, \cdot \rangle$. V posebnem karakterji še vedno tvorijo ortonormiran sistem vektorjev v $\fun(G,\CC)$ in koeficienti razvoja razrednih funkcij po karakterjih se ne spremenijo.

<div class="domacanaloga">

Oglejmo si še eno uporabo restriktivnih vrednosti kompleksnih karakterjev. Naj bo $G$ končna grupa in $\rho$ njena poljubna *zvesta* končno razsežna kompleksna upodobitev. Tedaj obstaja $N$, tako da je vsaka nerazcepna kompleksna upodobitev grupe $G$ podupodobitev $\rho^{\otimes N}$.

Dokaza se lahko lotiš tako, da fiksiraš nerazcepno upodobitev $\pi \in \Irr(G)$ in opazuješ *rodovno funkcijo* večkratnosti, se pravi formalno vsoto $F(X) = \sum_{k = 0}^{\infty} \mult_{\rho^{\otimes k}}(\pi) X^k$. Dovolj bo premisliti, da je ta rodovna funkcija neničelna. Izrazi vsak koeficient $\mult_{\rho^{\otimes k}}(\pi)$ s pomočjo skalarnega produkta in se na ta način prepričaj, da ima $F(X)$ pol pri $X = 1/\deg \rho$, zato je res neničelna.

</div>

Osredotočimo se sedaj še na upodobitveni prostor. Naj bo $\rho$ kompleksna upodobitev grupe $G$ na končno razsežnem prostoru $V$. Izberimo bazo prostora $\{ v_i \}_{i}$ in z njo kompleksen skalarni produkt
```{math}
\left\langle \sum_i \alpha_i v_i, \sum_i \beta_i v_i \right\rangle = \sum_i \alpha_i \overline{\beta_i}.
```
Prostor $V$ je opremljen z linearnim delovanjem grupe $G$. Zdaj smo na ta prostor dodali strukturo skalarnega produkta in ni jasno, ali je grupa $G$ kompatibilna s to dodatno strukturo. Kadar je temu tako, se pravi
```{math}
\forall g \in G. \ \forall v, w \in V. \quad \langle \rho(g) \cdot v, \rho(g) \cdot w \rangle = \langle v, w \rangle,
```
tedaj rečemo, da je $\rho$ <span class="definicija">unitarna upodobitev</span>. V tem primeru $\rho$ slika iz $G$ v grupo unitarnih transformacij $\U(V)$ prostora $V$ s skalarnim produktom $\langle \cdot, \cdot \rangle$. Seveda ni vsaka upodobitev končne grupe unitarna,[^17] je pa vsaka upodobitev *unitarizabilna*.

<div class="trditev">

Naj bo $G$ končna grupa in $\rho$ njena končno razsežna kompleksna upodobitev na prostoru $V$. Tedaj na $V$ obstaja skalarni produkt, glede na katerega je $\rho$ unitarna.

</div>

<div class="dokaz">

Izberimo poljuben skalarni produkt $\langle \cdot, \cdot \rangle$ na $V$ in ga povprečimo do
```{math}
\langle \cdot, \cdot \rangle_0 \colon V \times V \to \CC, \quad
    \langle v, w \rangle_0 = \frac{1}{|G|} \sum_{g \in G} \langle \rho(g) \cdot v, \rho(g) \cdot w \rangle.
```
Ni težko preveriti, da je $\langle \cdot, \cdot \rangle_0$ skalarni produkt na $V$, glede na katerega je $\rho$ unitarna upodobitev.

</div>

V kontekstu kompleksnih upodobitev končnih grup lahko torej brez škode predpostavimo, da je prostor opremljen s skalarnim produktom, glede na katerega je dana upodobitev unitarna.

<div class="zgled">

Končna grupa deluje z regularno upodobitvijo $\rho_{\fun}$ na prostoru funkcij $\fun(G, \CC)$. Ta prostor je opremljen s standardnim kompleksnim skalarnim produktom. Glede na ta skalarni produkt je $\rho_{\fun}$ unitarna upodobitev, saj za vsaka $f,h \in \fun(G,\CC)$ in $x \in G$ velja
```{math}
\left\langle \rho_{\fun}(x) \cdot f, \rho_{\fun}(x) \cdot h  \right\rangle =
    \frac{1}{|G|} \sum_{g \in G} f(gx) \overline{h(gx)}
    = \langle f, h \rangle.
```

</div>

Unitarnost upodobitev končne grupe $G$ lahko izkoristimo pri Fourierovi transformaciji. Za unitarno upodobitev $\rho$ je namreč $\rho(g^{-1}) = \rho(g)^*$ za vsak $g \in G$ in s tem
```{math}
\hat{f}(\rho) = \sum_{g \in G} f(g) \rho(g)^*.
```
Opremljeni s tem komentarjem se obrnimo k Fourierovi inverziji. Formula za razvoj funkcije $f \in \fun(G,\CC)$ po $\pi$-izotipičnih komponentah je nekoliko asimetrična. To lahko popravimo tako, da jo uteženo povprečimo z neko drugo funkcijo $h \in \fun(G,\CC)$. Dobimo
```{math}
\sum_{g \in G} f(g) \overline{h(g)} = \frac{1}{|G|} \sum_{\pi \in \Irr(G)} \sum_{g \in G} \overline{h(g)} \chi_{\pi}(1) \tr \left( \hat{f}(\pi) \cdot \pi(g) \right),
```
kar lahko po upoštevanju linearnosti sledi in gornjega komentarja glede unitarnosti upodobitve $\pi$ zapišemo kot
```{math}
\langle f, h \rangle = \frac{1}{|G|^2} \sum_{\pi \in \Irr(G)} \chi_{\pi}(1) \tr(\hat{f}(\pi) \cdot \hat{h}(\pi)^*).
```
Tej enakosti rečemo <span class="definicija">Parsevalov izrek</span>. Nekoliko pregledneje ga lahko zapišemo z uporabo še enega skalarnega produkta, tokrat na prostoru endomorfizmov danega vektorskega prostora $V$. Za linearni preslikavi $A,B \in \hom(V,V)$ definiramo
```{math}
\langle A, B \rangle_{\HS} = \tr(A \cdot B^*),
```
to je <span class="definicija">Hilbert-Schmidtov skalarni produkt</span>. Parsevalov izrek nam torej povezuje standarden kompleksni skalarni produkt funkcij s Hilbert-Schmidtovim skalarnim produktom Fourierovih transformacij v nerazcepnih upodobitvah,
```{math}
\langle f, h \rangle = \frac{1}{|G|^2} \sum_{\pi \in \Irr(G)} \chi_{\pi}(1) \left\langle \hat{f}(\pi), \hat{h}(\pi) \right\rangle_{\HS}.
```

[^1]: Tukaj uporabljamo verjetnostno oznako za povprečno vrednost. Mislimo si, da enakomerno naključno izberemo element $X$ iz grupe $G$ in v njem izračunamo vrednost $f$. Število $\EE(f)$ je pričakovana vrednost slučajne spremenljivke $f(X)$.

[^2]: Spomnimo se, da je delovanje $G$ na $\hom(V,V)$ dano kot $g \cdot \Phi = \rho(g) \Phi \rho(g)^{-1}$ za $g \in G$, $\Phi \in \hom(V,V)$.

[^3]: V tem primeru sicer nimamo dostopa do povprečenja v celoti, lahko pa uporabimo *delno* povprečenje, ki izračuna le vsoto po grupi.

[^4]: In najverjetneje taka korespondenca v splošnem *ne* obstaja. Je pa na voljo za kakšne posebne družine grup, kot bomo spoznali kasneje.

[^5]: <span class="definicija">Komutator</span> elementov $x,y \in G$ je element $[x,y] = x^{-1} y^{-1} x y$. <span class="definicija">Komutatorska podgrupa</span> grupe $G$ je $[G,G] = \langle [x,y] \mid x,y \in G \rangle$.

[^6]: Pri tem fiksne točke permutacije obravnavamo kot cikle dolžine $1$.

[^7]: Relaciji sta ortogonalni v smislu tabele karakterjev. Ortonormiranost karakterjev preberemo tako, da fiksiramo vrstice. To drugo relacijo pa preberemo tako, da fiksiramo stolpce. Tej relaciji včasih rečemo <span class="definicija">druga ortogonalnostna relacija</span>.

[^8]: Zanimivo je, da smo uspeli določiti tabelo karakterjev, brez da bi eksplicitno poznali vse upodobitve.

[^9]: V asociativni algebri to izrečemo ponavadi takole: vsak levi ideal v polenostavni algebri je glavni.

[^10]: Za endomorfizem $A$ je $\Eigenspace_\lambda(A)$ lastni podprostor $A$ za lastno vrednost $\lambda$.

[^11]: Na podoben način lahko določimo tudi upodobitve same, ne le karakterje.

[^12]: GAP je programski jezik, ki pride zelo prav pri delu z grupami, saj ima implementiranih veliko standardnih konstrukcij grup in funkcij za delo z njimi. Dostopen je prosto na naslovu <https://www.gap-system.org>. Osnovna načela za delo z upodobitvami končnih grup lahko najdeš v [Moravčevi skripti](https://users.fmf.uni-lj.si/moravec/Papers/upodob_moravec.pdf).

[^13]: Iz argumenta vidimo, da velja celo naslednje. Končna grupa $G$ je enostavna, če in samo če je vsaka njena netrivialna nerazcepna upodobitev zvesta.

[^14]: Virtualnih, ker vsebuje tudi negativne kombinacije nerazcepnih kolobarjev, ki ne ustrezajo karakterjem upodobitev.

[^15]: <span class="definicija">Algebraično celo število</span> je kompleksno število, ki je ničla moničnega polinoma s celoštevilskimi koeficienti. Množico algebraičnih celih števil označimo z $\bar{\ZZ}$. Ni se težko prepričati, da $\bar{\ZZ}$ tvori kolobar in da velja $\QQ \cap \bar{\ZZ} = \ZZ$.

[^16]: Diagonalizabilnost sledi iz obravnave Jordanove normalne forme preslikave $\rho(g)$.

[^17]: Skalarni produkt na danem prostoru lahko izberemo na mnogo različnih načinov.


## Kviz

```{raw} html
<div class="quiz-item" data-correct="true">
```

Vsaka nerazcepna upodobitev končne grupe je končnorazsežna.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Vsaka upodobitev končne grupe je polenostavna.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Končna $p$-grupa ima nad poljem karakteristike $p$ lahko neskončno mnogo nerazcepnih upodobitev.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Tedaj se vsaka nerazcepna upodobitev $G$ pojavi v regularni upodobitvi z večkratnostjo $\deg(\pi)$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Matrični koeficienti neizomorfnih nerazcepnih upodobitev končne grupe nad ugodnim poljem so ortogonalni.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Kompleksni nerazcepni karakterji končne grupe $G$ tvorijo ortonormiran sistem v prostoru kompleksnih funkcij na $G$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Nekomutativna Fourierova transformacija funkcije $f$ na grupi $G$ v upodobitvi $\pi$ je $\hat{f}(\pi) = \sum_{g \in G} f(g) \pi(g)$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Za vsako funkcijo $f$ na grupi $G$ velja $\hat{f}(\rho_{fun}) \cdot 1_1 = f$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Naj bo $G$ končna grupa in $F$ algebraično zaprto polje karakteristike tuje $|G|$. Fourierova transformacija razredne funkcije $f$ na $G$ v regularni upodobitvi je skalarno množenje.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Število nerazcepnih kompleksnih upodobitev končne grupe $G$ je enako $k(G)$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Konjugiranostni razredi v simetrični grupi $S_n$ so v bijekciji z razčlenitvami števila $n$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Naj bo $G$ končna grupa in $\rho$ njena končnorazsežna kompleksna upodobitev. Tedaj je $\rho$ nerazcepna, če in samo če velja $|| \chi_{\rho} || = 0$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Vsaka endospletična regularne upodobitve končne grupe nad kompleksnimi števili izhaja iz Fourierove transformacije.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Funkcija $f \in \mathrm{fun}(G,\mathbf{C})$ je izračunljiva iz svojih Fourierovih transformirank v nerazcepnih upodobitvah.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Tabelo karakterjev simetrične grupe $S_n$ nad poljem kompleksnih števil lahko izračunamo z algoritmom, ki teče v polinomskem času v odvisnosti od $n$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Kolobar virtualnih karakterjev $R(G)$ dane končne grupe je končno generiran kot kolobar.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Naj bo $G$ končna grupa. Karakter vsake končnorazsežne kompleksne upodobitve grupe $G$ je celoštevilska linearna kombinacija indukcij nerazcepnih karakterjev podgrup $G$ praštevilske moči.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Stopnja nerazcepne kompleksne upodobitve končne grupe deli moč grupe.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Vsaka kompleksna upodobitev končne grupe je unitarna.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Parsevalov izrek povezuje standardni kompleksni skalarni produkt na prostoru funkcij s Hilbert-Schmidtovimi skalarnimi produkti Fourierovih transformirank v nerazcepnih upodobitvah.

```{raw} html
</div>
```
