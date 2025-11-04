```{raw} html
<style>
  body { counter-reset: chapter 4 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Uporabe

Avstralski matematik Geordie Williamson je na svojem [plenarnem predavanju](https://www.youtube.com/watch?v=-3q6C558yog) na Mednarodnem matematičnem kongresu leta 2018 opisal teorijo upodobitev na naslednji način.

*The idea is that groups in mathematics are everywhere, but groups are nonlinear objects and are rather complicated. We attempt to linearize in some way by taking, for example, actions on a space of functions. We understand what can happen in the linear world by representation theory. Then we hope to go back to our original problem.*

V tem poglavju si bomo pogledali nekaj konkretnih aplikacij teorije upodobitev, ki na prvi pogled nimajo nobene povezave z upodobitvami, nazadnje pa je za njihovo razumevanje ključna. Pričeli bomo z abelovimi grupami. V tem primeru aplikacijam teorije upodobitev ponavadi rečemo <span class="definicija">harmonična analiza</span>. To zgodbo bomo potem razširili še v nekomutativen svet.

## Aritmetična zaporedja

### Aritmetična zaporedja v gostih množicah

Za poljuben $n \in \NN$ opazujmo množico celih števil $\{ 1, 2, \dots, n \}$ . Vsaki njeni podmnožici $A$ lahko priredimo gostoto $\delta = |A|/n$. Kadar je $A$ visoke gostote, pričakujemo, da bomo v njej lahko našli veliko vzorcev različnih vrst, ki upoštevajo strukturo seštevanja ali množenja v množici celih števil. Eden od temeljnih takih vzorcev v množici celih števil so <span class="definicija">aritmetična zaporedja</span>, se pravi zaporedja oblike
```{math}
x, \ x+y, \ x+2y, \dots, \ x + (k-1)y
```
za $x,y \in \ZZ$, $k \in \NN$. Število $k$ je dolžina tega zaporedja in opazujemo seveda le zaporedja dolžine vsaj $3$. Izkaže se, da je ta struktura vselej prisotna, neodvisno od izbire konkretne množice $A$, če je le $n$ dovolj velik in gostota $\delta$ pozitivna.

<div class="izrek">

Naj bosta $k \geq 3$ in $\delta > 0$. Tedaj za vse dovolj velike $n \in \NN$ velja, da vsaka podmnožica $A \subseteq \{ 1, 2, \dots, n \}$ gostote vsaj $\delta$ vsebuje aritmetično zaporedje dolžine $k$.

</div>

Dokaz tega izreka je kombinatoričen in tehnično precej zahteven. Mi si bomo ogledali poseben primer za $k = 3$, torej za obstoj $3$-členih aritmetičnih zaporedij. Za ta primer bomo izpeljali celo nekoliko močnejšo izjavo, katere dokaz bo slonel na teoriji upodobitev.

<div class="izrek">

Za neko konstanto $C$ in za vse dovolj velike $n \in \NN$ velja, da vsaka podmnožica $A \subseteq \{ 1, 2, \dots, n \}$ gostote vsaj $C/\log \log n$ vsebuje aritmetično zaporedje dolžine $3$.

</div>

### Harmonična analiza

#### Projekcija v $\FF_p$

Rothov izrek se sicer tiče podmnožice celih števil, ampak ker to množico filtriramo s podmnožicami $\{1,2,\dots,n\}$, lahko izberemo neko praštevilo $p \geq n$ in dogajanje opazujemo v projekciji na kvocient $\ZZ/p\ZZ = \FF_p$. Pri tem moramo biti nekoliko previdni, saj so aritmetična zaporedja v $\FF_p$ lahko nekoliko nenavadna.

<div class="zgled">

Naj bo $p > 2$. V $\FF_p$ tvori množica $\{ 0, 1, (p+1)/2 \}$ aritmetično zaporedje. Res, če vzamemo $x = 0$, $y = (p+1)/2$, potem dobimo zaporedje z razliko $y$ kot
```{math}
x = 0, \ x + y = \frac{p+1}{2}, \ x + 2y = p + 1 = 1.
```

</div>

Če torej rešimo Rothov problem za podmnožice $\FF_p$ namesto za podmnožice $\{1,2,\dots,n\}$, moramo biti previdni, saj dobljenega aritmetičnega zaporedja morda ne bomo mogli dvigniti iz $\FF_p$ v $\ZZ$. Tej težavi se lahko izognemo tako, da izberemo praštevilo $p$ z lastnostjo $p > 2n$. Ni se težko prepričati, da v tem primeru vsako aritmetično zaporedje s $3$ členi v $\{ 1, 2, \dots, n \} \subseteq \FF_p$ lahko dvignemo do aritmetičnega zaporedja v $\{1,2,\dots,n\}$. Poleg tega želimo, da se gostota množice $A$ pri projekciji iz $\{1,2,\dots,n \}$ v $\FF_p$ ne spremeni preveč, zato praštevilo $p$ ne sme biti preveliko. Optimalna izbira bo torej praštevilo $p$ z lastnostjo $2n < p < 4n$, taka izbira pa tudi vselej obstaja po [Bertrandovem postulatu](https://sl.wikipedia.org/wiki/Bertrandova_domneva).

Dogajanje smo na ta način prestavili v končno abelovo grupo $\FF_p$. V njej opazujemo množico $A \subseteq \FF_p$, ki je gostote $\delta$. Dokazati želimo, da za dovolj velik $p$ obstajajo v $A$ aritmetična zaporedja dolžine $3$, če je le $\delta > C/\log \log p$ za neko konstanto $C$.

#### Izražanje problema v jeziku upodobitev

Rothov izrek v $\FF_p$ napadimo z močnimi orodji teorije upodobitev grupe $\FF_p$. Problem bomo najprej izrazili v prostoru funkcij $\fun(\FF_p, \CC)$. Naj bo $1_A$ karakteristična funkcija množice $A$. Vsako aritmetično zaporedje dolžine $3$ je oblike $x,z,y$, pri čemer je $z-x = y-z$, kar je enakovredno $x+y=2z$. Števila $x$, $y$ in $(x+y)/2$ morajo torej pripadati množici $A$. Število aritmetičnih zaporedij dolžine $3$ v $A$ lahko zato izrazimo kot
```{math}
\sum_{x,y,z \in \FF_p : x+y=2z} 1_A(x) 1_A(y) 1_A(z)
    = \sum_{z \in \FF_p} \left( 1_A * 1_A \right)(z) 1_A(z/2)
```
Naj bo $1_{2A}(z) = 1_A(z/2)$. Zadnjo vsoto prepoznamo kot skalarni produkt
```{math}
p \cdot \langle 1_A * 1_A, 1_{2A} \rangle,
```
kar lahko s Parsevalovim izrekom razvijemo kot
```{math}
\frac{1}{p} \sum_{\chi \in \Irr(\FF_p)} \widehat{1_A*1_A}(\chi) \overline{\widehat{1_{2A}}(\chi)}.
```
Trikrat globoko vdihnimo in premislimo vsako zadevo posebej.

1.  Nerazcepne upodobitve oziroma karakterje grupe $\FF_p$ eksplicitno poznamo, enaki so
    ```{math}
    \chi_j \colon \FF_p \to \CC^*, \quad
        x \mapsto \zeta^{j x}
    ```
    za $j \in \FF_p$, kjer je $\zeta = e^{2 \pi i/p}$.

2.  Povezavo med konvolucijo in Fourierovo transformacijo smo videli že pri spletičnah. Dokazali smo, da vse endospletične regularne upodobitve izhajajo iz uporabe Fourierove transformacije. Te lastnosti smo kasneje uporabili tudi pri simetrični grupi. Naj bo zdaj $G$ poljubna grupa in $F$ polje. Naj bosta $f_1, f_2 \in \fun(G,F)$ funkciji in $\rho$ upodobitev grupe $G$. Kompozicija Fourierovih transformacij $\widehat{f_1}(\rho) \cdot \widehat{f_2}(\rho)$ je enaka
    ```{math}
    \sum_{g_1, g_2 \in G} f_1(g_1) f_2(g_2) \rho(g_1^{-1} g_2^{-1}) =
        \sum_{g \in G} (f_2 * f_1)(g) \rho(g^{-1}).
    ```
    Torej velja
    ```{math}
    \widehat{f_1}(\rho) \cdot \widehat{f_2}(\rho) =
        \widehat{f_2 * f_1}(\rho)
    ```
    in Fourierova transformacija pretvarja konvolucijo funkcij v produkt linearnih preslikav, pri čemer moramo biti pozorni na vrstni red operacij zaradi morebitne nekomutativnosti grupe.

3.  Velja
    ```{math}
    \widehat{1_{2A}}(\chi) = \sum_{g \in \FF_p} 1_{2A}(g) \chi(-g)
        = \sum_{x \in \FF_p} 1_A(x) \chi(-2x)
        = \widehat{1_A}(\chi^2).
    ```

Število iskanih aritmetičnih zaporedij je zato enako
```{math}
\frac{1}{p} \sum_{j \in \FF_p} \widehat{1_A}(\chi_j)^2 \overline{\widehat{1_A}(\chi_j^2)}
    = \frac{1}{p} \sum_{j \in \FF_p} \widehat{1_A}(\chi_j)^2 \widehat{1_A}(\chi_{-2j})
```

#### Glavni del in prispevki netrivialnih karakterjev

Izolirajmo prispevek trivialne upodobitve. Velja $\widehat{1_A}(\chi_0) = \widehat{1_A}(\oneone) = |A|$, zato je število aritmetičnih zaporedij dolžine $3$ v $A$ enako
```{math}
\frac{|A|^3}{p} +  \frac{1}{p} \sum_{j \in \FF_p^*} \widehat{1_A}(\chi_j)^2 \widehat{1_A}(\chi_{-2j}).
```
Glavni del rezultata je nekoliko nehomogen. To lahko popravimo z dodatno normalizacijo s $p^2$, ki ima pravzaprav zelo smiselno interpretacijo. Če namreč izberemo $x,y,z \in \FF_p$ enakomerno naključno, a pogojno na veljavnost $x+y=2z$,[^1] potem je verjetnost, da so $x,y,z$ vsi v $A$, enaka
```{math}
\PP_{x,y,z \in \FF_p}(x,y,z \in A \mid x+y=2z) =
    \delta^3 + \frac{1}{p^3} \sum_{j \in \FF_p^*} \widehat{1_A(\chi_j)}^2 \widehat{1_A}(\chi_{-2j}).
```
Brez pogojne omejitve bi bila zgornja verjetnost seveda enaka $\delta^3$. Srčika pogoja aritmetičnega zaporedja dolžine $3$ se torej skriva v prispevkih netrivialnih karakterjev. Splošna strategija harmonične analize je, da ti prispevki nikdar ne uspejo izničiti glavnega delta $\delta^3$ in da v $A$ torej res obstaja aritmetično zaporedje dolžine $3$.

Za omejitev netrivialnih prispevkov najprej uporabimo trikotniško neenakost,
```{math}
\left| \sum_{j \in \FF_p^*} \widehat{1_A}^2(\chi_j) \widehat{1_A}(\chi_{-2j}) \right|
    \leq \max_{j \in \FF_p^*} |\widehat{1_A}(\chi_j)| \cdot 
    \sum_{j \in \FF_p^*} 
    |\widehat{1_A}(\chi_j)|
    |\widehat{1_A}(\chi_{-2j})|.
```
Zadnjo vsoto ocenimo s Cauchy-Schwartzovo neenakostjo, tako da dobimo zgornjo mejo
```{math}
\max_{j \in \FF_p^*} |\widehat{1_A}(\chi_j)| \cdot 
    \sqrt{\sum_{j \in \FF_p} |\widehat{1_A}(\chi_j)|^2} \cdot \sqrt{\sum_{j \in \FF_p} |\widehat{1_A}(\chi_{-2j})|^2}.
```
Vsota pod korenoma je v obeh primerih enaka, in sicer jo po Parsevalu lahko izrazimo kot
```{math}
\sum_{j \in \FF_p} |\widehat{1_A}(\chi_j)|^2
    = \sum_{j \in \FF_p} \langle \widehat{1_A}(\chi_j), \widehat{1_A}(\chi_j) \rangle_{\HS}
    = p^2 \langle 1_A, 1_A \rangle = p |A|.
```
Od tod torej sklenemo
```{math}
\PP_{x,y,z \in \FF_p}(x,y,z \in A \mid x+y=2z)
    \geq \delta^3 - \delta \cdot \frac{1}{p} \max_{j \in \FF_p^*} |\widehat{1_A}(\chi_j)|.
```
Kadar je Fourierova transformacija $1_A$ v vseh netrivialnih karakterjih strogo manjša od $p \delta^2$, je verjetnost na levi strani strogo pozitivna, zato res najdemo aritmetično zaporedje dolžine $3$ v $A$. Ko pa ima po drugi strani $\widehat{1_A}$ kakšen velik netrivialen Fourierov koeficient, se pravi ko za nek $j \in \FF_p^*$ velja
```{math}
|\widehat{1_A}(\chi_j)| \geq p \delta^2,
```
pa harmonična analiza odpove. V tem primeru moramo podrobneje raziskati pomen velikega Fourierovega koeficienta.

#### Večanje gostote

Predpostavimo, da je $|\widehat{1_A}(\chi_j)| \geq p \delta^2$ za nek $j \in \FF_p^*$. Preden nadaljujemo, bomo funkcijo $1_A$ projicirali na podprostor funkcij z ničelnim povprečjem. Naj bo $f = 1_A - \delta \in \fun(\FF_p, \CC)$. Velja
```{math}
\widehat{f}(\chi_j) = \widehat{1_A}(\chi_j) - \delta \widehat{1}(\chi_j)
    = \widehat{1_A}(\chi_j) - \delta p \langle \oneone, \chi_j \rangle
    = \widehat{1_A}(\chi_j),
```
zato je
```{math}
\left|\sum_{x \in \FF_p} f(x) \zeta^{-jx}\right| = |\widehat{f}(\chi_j)| \geq p \delta^2.
```
Funkcija $x \mapsto \zeta^{-jx}$ precej oscilira, ko $x$ preteče ves $\FF_p$. Če bi bila ta funkcija približno konstanta, bi lahko sklepali, da je vsota vrednosti $f$ precej velika. Približno konstantnost te funkcije lahko dosežemo tako, da preidemo na neko podmnožico $\FF_p$.

<div class="domacanaloga">

Obstaja konstanta $c \in (0,\frac12)$, za katero velja naslednje. Množico $\FF_p$ lahko razčlenimo kot disjunktno unijo množice podmnožic $P_1, P_2, \dots, P_m$, tako da je vsaka množica $P_i$ aritmetično zaporedje dolžine med $c \sqrt{p}$ in $(1-c) \sqrt{p}$, hkrati pa je $|\zeta^{-jx} - \zeta^{-jy}| < c \delta^2$ za vsaka $x,y \in P_i$.

</div>

S pomočjo razčlenitve množice $\FF_p$ torej sklepamo
```{math}
\left|\sum_{x \in \FF_p} f(x) \zeta^{-jx}\right| \leq
   \sum_{i = 1}^m \left| \sum_{x \in P_i} f(x) \zeta^{-jx} \right|
   = \sum_{i = 1}^m \left| \sum_{x \in P_i} f(x) \left( \zeta^{-jx_0} + (\zeta^{-jx} - \zeta^{-jx_0}) \right) \right|,
```
kjer smo v vsakem $P_i$ izbrali nek element $x_0$. Po trikotniški neenakosti in upoštevanju približne konstantnosti funkcije $x \mapsto \zeta^{-jx}$ na $P_i$ lahko zadnjo vsoto omejimo navzgor kot
```{math}
\sum_{i = 1}^m \left| \sum_{x \in P_i} f(x) \right| + 
    \sum_{i = 1}^m \sum_{x \in P_i} | f(x) | c \delta^2
    \leq \sum_{i = 1}^m \left| \sum_{x \in P_i} f(x) \right| + c p \delta^2.
```
S tem nazadnje dobimo neenakost
```{math}
\sum_{i = 1}^m \left| \sum_{x \in P_i} f(x) \right| \geq (1-c) p \delta^2.
```
Po konstrukciji je povprečje funkcije $f$ po $\FF_p$ enako $0$. Vsote po zaporedjih $P_i$ se torej seštejejo v $0$, po absolutni vrednosti pa se seštejejo v vsaj $(1-c) p \delta^2$. Torej obstaja nek $i$, za katerega velja
```{math}
\sum_{x \in P_i} f(x)
    +
    \left| \sum_{x \in P_i} f(x) \right|
     \geq \frac{1}{m} (1-c) p \delta^2.
```
Ker je $|\FF_p| = \sum_{i = 1}^m |P_i|$, dobimo neenakost $p \geq m c \sqrt{p}$. Hkrati za vsako realno število $r$ velja $r + |r| = 2 \max(r, 0)$, zato je
```{math}
\max \left( \sum_{x \in P_i} f(x), 0 \right) \geq
    \frac{c (1-c)}{2}  \sqrt{p} \delta^2
    \geq \frac{c}{2} |P_i| \delta^2.
```
Leva stran je zato strogo pozitivna in enaka vsoti $f$ po $P_i$. Upoštevamo še $f = 1_A - \delta$ in sklenemo
```{math}
|A \cap P_i| \geq \frac{c}{2} |P_i| \delta^2 + |P_i| \delta
```
oziroma ekvivalentno
```{math}
\frac{|A \cap P_i|}{|P_i|} \geq \delta + \frac{c}{2} \delta^2.
```
Množica $A$ ima torej v aritmetičnem zaporedju $P_i$ gostoto za $\frac{c}{2} \delta^2$ večjo kot v $\FF_p$.

#### Iteracija

Povzemimo. Če množica $A$ gostote $\delta$ nima aritmetičnih zaporedij dolžine $3$, potem smo našli aritmetično zaporedje $P_i$, v katerem ima $A$ gostoto vsaj $\delta + \frac{c}{2} \delta^2$. Ta postopek zdaj iteriramo.[^2] Če množica $A \cap P_i$ nima aritmetičnih zaporedij dolžine $3$, potem najdemo aritmetično zaporedje dolžine med $c\sqrt{|P_i|}$ in $(1-c)\sqrt{|P_i|}$, v katerem ima $A$ gostoto vsaj $\delta + 2 \frac{c}{2} \delta^2$, in tako dalje. Ker gostota na nobeni točki ne more preseči vrednosti $1$, se ta postopek gotovo ustavi po končno mnogo korakih. Na tej točki najdemo aritmetično zaporedje dolžine $3$ v $A$, če je le velikost množice $P_i$ do te točke dovolj velika. Iz podrobne analize večanja gostote in spreminjaja velikosti množic $P_i$ se da izpeljati,[^3] da ta argument res deluje, če je le $\delta \geq C/\log \log p$ za neko konstanto $C$. S tem je Rothov izrek dokazan.

### Onkraj Rothovega izreka

Mnogo dela po Rothovem izreku je bilo posvečenega izboljšanju meje o gostoti, ki še zagotovi obstoj aritmetičnih zaporedij dolžine $3$. Večina izboljšav spodnje meje je s sabo prinesla nove ideje, uporabne tudi za reševanje kakšnih drugih problemov. Najsodobnejši rezultat v zvezi s tem je prebojen članek [(Bloom-Sisask 2020)](https://www.quantamagazine.org/landmark-math-proof-clears-hurdle-in-top-erdos-conjecture-20200803/), kjer avtorja dokažeta, da obstajata konstanti $C,c$, tako da ima vsaka množica $A \subseteq \{ 1, 2, \dots, n \}$ gostote vsaj $C / (\log n)^{1 + c}$ aritmetično zaporedje dolžine $3$. Ta meja se torej znebi dvojnega logaritma in uvede minimalen eksponent k logaritmu, zato je bistveno manjša restrikcija na gostoto.[^4]

Ta rezultat lahko uporabimo, na primer, z množico praštevil. Po izreku Čebiševa je število praštevil do $n$ vsaj $C n / \log n$, zato imajo praštevila v $\{1,2,\dots,n\}$ gostoto vsaj $C / \log n$ in na njih lahko apliciramo posplošeni Rothov izrek. Ker lahko vselej tudi izpustimo prvih nekaj praštevil, torej sklepamo, da množica praštevil vsebuje neskončno mnogo aritmetičnih zaporedij dolžine $3$. Poudarimo konceptualno pomembno dejstvo, da smo ta rezultat izpeljali zgolj zaradi same gostote praštevil in ne zaradi kakršne koli druge njihove lastnosti. Nenazadnje je slogan izvirnega Rothovega izreka ta, da lahko najdemo v vsaki dovolj gosti množici strukturo.

<div class="odprtproblem">

Ali je mogoče z ustrezno posplošitvijo Rothovega izreka dokazati, da praštevila vsebujejo aritmetična zaporedja dolžine $k$ za vsak $k \geq 3$? Obstoj takih zaporedij je sicer znan iz [(Green-Tao 2004)](https://en.wikipedia.org/wiki/Green–Tao_theorem), ki temelji na razširitvi Szemerédijevega izreka, a ne v smeri nižanja meje gostote, temveč v uporabi izreka na specifičnih redkih podmnožicah.

</div>

<div class="domacanaloga">

S harmonično analizo dokaži, da ima za vsak $n \geq 3$ Fermatova enačba $x^n + y^n = z^n$ netrivialno ($xyz \neq 0$) rešitev v $\FF_p$ za vsako dovolj veliko (v odvisnosti od $n$) praštevilo $p$. Eden izmed pristopov je, da število rešitev enačbe izraziš s Fourierovo inverzijo funkcije $1_0$ v aditivni grupi $\FF_p$ kot
```{math}
\sum_{x,y,z \in \FF_p} 1_{0}(x^n + y^n - z^n)
    = \frac{1}{p} \sum_{x, y, z, j \in \FF_p} \zeta^{j(x^n + y^n - z^n)}
    = \frac{1}{p} \sum_{j \in \FF_p} S_j \cdot S_j \cdot \overline{S_j},
```
kjer je $S_j = \sum_{a \in \FF_p} \zeta^{j a^n}$. Določi glavni del ter omeji prispevke netrivialnih karakterjev.

</div>

## Podmnožice brez produktov

### Antipodgrupe

Naj bo $G$ končna grupa in $A \subseteq G$ njena podmnožica. Množica $A$ je podgrupa, če in samo če je zaprta za množenje, se pravi $A \cdot A \subseteq A$. Skrajno diametralno tej strukturi se znajdemo, če predpostavimo, da produkt *nobenih* dveh elementov iz množice $A$ ne pripada $A$, se pravi $A \cdot A \cap A = \emptyset$. Z drugimi besedami, enačba $xy = z$ v množici $A$ nima rešitev. V tem primeru rečemo, da je množica $A$ <span class="definicija">brez produktov</span>. Če smo v teoriji grup malodane obsedeni s strukturiranimi množicami, nas mora vsaj malo tudi zanimati tudi druga skrajnost.

Kadar množica $A$ vsebuje kakšno podgrupo, seveda *ni* brez produktov, zato se morajo take množice čim bolj izogniti podgrupam. Osnovno vprašanje v zvezi z množicami brez produktov je, kako velike podmnožice brez produktov dana grupa vsebuje. Za začetek si oglejmo nekaj preprostih zgledov.

<div class="zgled">

- Naj bo $G = \ZZ/n\ZZ$ in $A$ neka njena podmnožica. Množica $A$ je brez produktov, če in samo če enačba $x+y=z$ nima rešitve v $A$. To vprašanje je ravno obratno sorodni lastnosti, ki smo jo opazovali v prejšnjem razdelku. Tam smo reševali le malo drugačno enačbo $x+y=2z$ in dokazali, da ima vselej rešitve v podmnožicah pozitivne gostote. Zanimivo je, da je situacija precej drugačna za enačbo $x+y = z$.[^5] Za množico $A$ lahko vzamemo na primer vsa števila v $\ZZ/n\ZZ$, ki so strogo med $\frac{1}{3}n$ in $\frac{2}{3}n$. Ta množica je jasno brez produktov in je gostote približno $\frac{1}{3}$ v $\ZZ/n\ZZ$ za velike vrednosti $n$.

  To konstrukcijo lahko posplošimo na poljubno končno abelovo grupo.

  <div class="domacanaloga">

  Naj bo $A$ končna abelova grupa. Prepričaj se, da vselej obstaja podmnožica v $A$, ki je brez produktov in gostote vsaj $\frac{2}{7}$.

  </div>

- Simetrična grupa $S_n$ vsebuje ogromno množico brez produktov, in sicer množico vseh lihih permutacij $S_n \backslash A_n$. Produkt dveh lihih permutacij je soda permutacija, zato je ta množica res brez produktov. Njena gostota je $\frac12$.

- Naj bo $G$ končna grupa s podgrupo $H \leq G$. Naj bo $A = Hg$ za nek $g \in G \backslash H$. Tedaj za $x = h_1 g$ in $y = h_2 g$ velja $Hxy = Hh_1 g h_2 g = H g h_2 g$. Pri tem velja $xy \in A$, če in samo če je $H g h_2 g = Hg$, kar se poenostavi do $g h_2 \in H$, se pravi $g \in H$, kar je sprto s predpostavko. Množica $A$ je zato brez produktov. Njena gostota v $G$ je $1/|G:H|$. Ta primer posploši zadnjega, kjer smo obravnavali $A_n \leq S_n$.

</div>

Mnogo težje je najti podmnožice brez produktov pozitivne gostote v alternirajoči grupi $A_n$ (ko gre $n$ proti neskončnosti) ali linearni grupi $\PSL_2(\FF_p)$ (ko gre $p$ proti neskončnosti). Dokazali bomo, da to težavo lahko pojasnimo s teorijo upodobitev.

<div class="izrek">

Naj bo $G$ končna grupa in naj bo $m$ najmanjša stopnja netrivialne nerazcepne kompleksne upodobitve $G$. Tedaj je vsaka podmnožica brez produktov v $G$ gostote kvečjemu $m^{-1/3}$.

</div>

<div class="zgled">

- Iz rezultatov o upodobitvah simetričnih grup (natančneje, formule o kljukah) sledi, do ima $S_n$ dve nerazcepni upodobitvi stopnje $1$ (to sta $\oneone$ in $\sgn$) in dve nerazcepni upodobitvi stopnje $n-1$ (to sta $\rho$ in $\rho \otimes \sgn$), vse ostale nerazcepne upodobitve pa so višje stopnje (za $n \geq 7$). Velja torej $m = \Theta(n)$.[^6] Po izreku v $A_n$ zatorej *ni* podmnožic brez produktov pozitivne gostote, ko gre $n$ čez vse meje. Še več, največja dovoljena gostota je velikostnega reda $m^{-1/3} = \Theta(n^{-1/3})$.

- Opazujmo grupo $\PSL_2(\FF_p)$. Iz njene tabele karakterjev razberemo, da zanjo velja $m = (p-1)/2$. Po izreku tudi ta grupa nima podmnožic brez produktov pozitivne gostote, ko gre $p$ čez vse meje. Še več, največja gostota, ki jo dopušča izrek, je velikostnega reda $m^{-1/3} = \Theta(p^{-1/3}) = \Theta(|\PSL_2(\FF_p)|^{-1/9})$, kar je celo mnogo manjše (relativno glede na velikost grupe) od zgornje meje, ki smo jo videli v primeru alternirajoče grupe.

</div>

### Harmonična analiza

Gowersov izrek bomo dokazali s pomočjo nekoliko močnejše trditve.

<div class="trditev">

Naj bo $G$ končna grupa in naj bo $m$ najmanjša stopnja netrivialne nerazcepne kompleksne upodobitve $G$. Naj bosta $A,B \subseteq G$ podmnožici gostote $\alpha, \beta$. Tedaj velja
```{math}
\left| 
        \PP_{x,y,z \in G}(x,y \in A, \ z \in B \mid xy = z) - \alpha^2 \beta
    \right| 
    \leq
    m^{-1/2} \alpha \beta^{1/2}.
```

</div>

Iz trditve hitro izpeljemo Gowersov izrek. Uporabimo jo z $A=B$. Če je $A$ brez produktov in gostote $\alpha$, potem velja $\alpha^3 \leq m^{-1/2} \alpha^{3/2}$, kar je enakovredno $\alpha \leq m^{-1/3}$.

<div class="dokaz">

Verjetnost v trditvi je enaka
```{math}
\frac{|\{ (x,y,z) \in A \times A \times B \mid xy = z \}|}{|G|^2}.
```
Število rešitev enačbe $xy = z$ za $x,y \in A, z \in B$ lahko izrazimo kot
```{math}
\sum_{x,y,z \in G \colon xy = z} 1_A(x) 1_A(y) 1_B(z)
    = \sum_{z \in G} (1_A * 1_A)(z) 1_B(z)
    = |G| \cdot \langle 1_A * 1_A, 1_B \rangle.
```
Skalarni produkt razvijemo s Parsevalovo formulo in dobimo
```{math}
\frac{1}{|G|} \sum_{\pi \in \Irr(G)} \chi_{\pi}(1) \cdot \langle \widehat{1_A}(\pi)^2, \widehat{1_B}(\pi) \rangle_{\HS}.
```
Prispevek trivialne upodobitve je enak
```{math}
\langle \widehat{1_A}(\oneone)^2, \widehat{1_B}(\oneone) \rangle_{\HS}/|G| = |A|^2 |B| / |G| = \alpha^2 \beta |G|^2.
```
Prispevke netrivialnih upodobitev lahko s trikotniško neenakostjo po absolutni vrednosti omejimo navzgor kot
```{math}
\frac{1}{|G|} \sum_{\oneone \neq \pi \in \Irr(G)} \chi_{\pi}(1) \left| \langle \widehat{1_A}(\pi)^2, \widehat{1_B}(\pi) \rangle_{\HS} \right|,
```
kar je po Cauchy-Schwartzovi neenakosti kvečjemu
```{math}
\frac{1}{|G|} \sum_{\oneone \neq \pi \in \Irr(G)} \chi_{\pi}(1) || \widehat{1_A}(\pi) ||_{\HS}^2 || \widehat{1_B}(\pi) ||_{\HS}.
```
V zadnji vsoti zadnjo normo omejimo z maksimumom, da dobimo zgornjo mejo
```{math}
\max_{\oneone \neq \pi \in \Irr(G)} || \widehat{1_B}(\pi) ||_{\HS} \cdot 
    \frac{1}{|G|} \sum_{\oneone \neq \pi \in \Irr(G)} \chi_{\pi}(1) || \widehat{1_A}(\pi) ||_{\HS}^2,
```
Prvi člen lahko omejimo z neenakostjo
```{math}
m \cdot \max_{\oneone \neq \pi \in \Irr(G)} || \widehat{1_B}(\pi) ||^2_{\HS}
    \leq \sum_{\oneone \neq \pi \in \Irr(G)} \chi_{\pi}(1) ||\widehat{1_B}(\pi)||_{\HS}^2 
    \leq |G|^2 ||1_B||^2 = |B||G|
```
in zadnjo neenakost lahko uporabimo tudi za omejitev drugega člena. S tem dobimo zgornjo mejo
```{math}
\sqrt{\frac{|B||G|}{m}} \cdot |A| = m^{-1/2} \alpha \beta^{1/2} |G|^2
```
za prispevke netrivialnih upodobitev. Trditev je s tem dokazana.

</div>

Iz Gowersovega izreka sledi nekoliko presenetljiva lastnost dovolj velikih podmnožic.

<div class="posledica">

Naj bo $G$ končna grupa in naj bo $m$ najmanjša stopnja netrivialne neracepne kompleksne upodobitve $G$. Če je $A$ podmnožica $G$ gostote strogo večje od $m^{-1/3}$, potem je $A \cdot A \cdot A = G$.

</div>

<div class="dokaz">

Naj bo $g \in G$ in naj bo $B = g A^{-1} \subseteq G$. Množici $A$ in $B$ sta obe enake gostote, recimo $\alpha$. Velja $\alpha^3 > m^{-1}$, kar je enakovredno $m^{-1/2} \alpha^{3/2} < \alpha^3$. Iz trditve od tod sledi $A \cdot A \cap B \neq \emptyset$, zato je $g \in A \cdot A \cdot A$. Ker je bil $g$ poljuben, je $A \cdot A \cdot A = G$.

</div>

Ta lastnost velikih množic ima mnogo zelo relevantnih uporab v teoriji grup, na primer pri dokazovanju Babaijeve domeneve o premerih končnih enostavnih grup prek teorije približnih podgrup in pri raziskovanju slučajnih sprehodov,[^7] kot je razloženo v [(Breuillard 2013)](https://library.slmath.org/books/Book61/files/15breu.pdf).

### Največja možna gostota

Z Gowersovo zgornjo mejo za dovoljeno gostoto množice brez produktov se seveda lahko vprašamo, kako optimalna je ta meja. Z drugimi besedami, konstruirati želimo čim večje podmnožice brez produktov. V grupah $A_n$ in $\PSL_2(\FF_p)$ te gotovo ne bodo pozitivne gostote, ko gredo moči grup čez vse meje.

<div class="zgled">

Opazujmo alternirajočo grupo $A_n$, ki deluje na množici točk $\{ 1, 2, \dots, n \}$. Naj bo $T \subseteq \{2,3,\dots,n \}$ poljubna podmnožica velikosti $t$. Definirajmo množico permutacij
```{math}
S = \{ \sigma \in A_n \mid \sigma(1) \in T, \ \sigma(T) \cap T = \emptyset \}.
```
Vsaka permutacija v $S \cdot S$ preslika $1$ v $T^c$, zato je $S \cap S \cdot S = \emptyset$ in množica $S$ je brez produktov. Njena gostota v $A_n$ je enaka
```{math}
\frac{1}{n!/2} \cdot t \cdot \binom{n-t}{t} t! \cdot (n-t-1)! \cdot \frac{1}{2}
  = \frac{t (n-t)! (n-t-1)!}{n!(n-2t)!}
  = \frac{t}{n} \cdot \frac{\binom{n-t}{t}}{\binom{n-1}{t}}.
```
Z aproksimacijo $\binom{n}{t} \sim (\frac{ne}{t})^t e^{O(- t^2/2n)}$[^8] za $t = o(n)$ lahko zadnji izraz poenostavimo do
```{math}
\frac{t}{n} e^{O(t^2/n)}.
```
Optimalno vrednost dosežemo z izbiro $t \sim n^{1/2}$, takrat je gostota množice $S$ v $A_n$ enaka $\sim n^{-1/2}$.

</div>

Gowersov izrek zagotavlja, da gostota množice brez produktov v $A_n$ ne more biti večja od $\Theta(n^{-1/3})$. Po drugi strani pa imamo zgled podmnožice brez produktov gostote $\sim n^{-1/2}$. Katera od teh mej je bližje resnični največji možni gostoti podmnožice brez produktov v $A_n$? To vprašanje je bilo razrešeno nedavno v [(Keevash-Lifschitz-Minzer 2022)](https://arxiv.org/abs/2205.15191), kjer avtorji dokažejo, da je konstrukcija v zadnjem zgledu v resnici optimalna: če je $A \subseteq A_n$ brez produktov največje možne moči, potem je $A$ ali $A^{-1}$ enaka eni od množic iz zadnjega zgleda. Njihov dokaz temelji na ideji, ki smo jo videli v dokazu Rothovega izreka, in sicer bodisi s harmonično analizo dokažemo želeno bodisi ima indikatorska funkcija visoko korelacijo z določenimi nelinearnimi karakterji in je zaradi tega prisotna neka struktura.

Konstrukcija Kedlaya, ki smo jo prikazali, je z nekoliko dodatnega truda[^9] posplošljiva na vse podgrupe $G \leq S_n$, ki delujejo tranzitivno na množici $\{ 1,2,\dots, n\}$. Vsaka grupa, ki tranzitivno deluje na množici $n$ točk, ima torej podmnožico brez produktov gostote $\sim n^{-1/2}$. V posebnem to velja za grupo $\PSL_2(\FF_p)$, ki deluje tranzitivno na projektivni premici $\PP^1(\FF_p)$ s $p+1$ točkami. Na ta način dobimo podmnožico v $\PSL_2(\FF_p)$ brez produktov gostote $\Theta(p^{-1/2})$. Gowersov izrek nam tukaj daje zgornjo mejo $\Theta(p^{-1/3})$ za gostoto množice brez produktov. V tem primeru optimalna ocena za gostoto ni znana.

<div class="odprtproblem">

Kolikšna je gostota največje množice brez produktov v $\PSL_2(\FF_p)$, ko gre $p$ čez vse meje?

</div>

## Prepoznavanje komutatorjev

Oglejmo si še en čisto nekomutativen problem, ki na prvi pogled nima veliko skupnega s teorijo upodobitev, nazadnje pa se izkaže, da ga lahko popolnoma razrešimo, če le poznamo tabelo karakterjev grupe.

### Množica komutatorjev

Naj bo $G$ končna grupa in $K(G)$ njena podmnožica, ki sestoji iz elementov, ki so komutatorji v $G$, se pravi
```{math}
K(G) = \{ [x,y] \mid x,y \in G \}.
```
Ta množica v splošnem *ni* podgrupa.

<div class="zgled">

V programskem okolju GAP se ni težko prepričati, da je najmanjša[^10] grupa $G$, v kateri $K(G)$ ne sovpada komutatorsko podgrupo $[G,G] = \langle K(G) \rangle$, moči $96$. V GAP je ta grupa dostopna pod imenom `SmallGroup(96, 3)`. Podamo jo lahko v njeni permutacijski obliki kot podgrupo $S_{12}$, generirano s permutacijama
```{math}
x = (1 \ 3 \ 5)(2 \ 4 \ 6)(7 \ 11 \ 9)(8 \ 12 \ 10), \quad
    y = (3 \ 9 \ 4 \ 10)(5 \ 7)(6 \ 8)(11 \ 12).
```
Hitro izračunamo, da je $|K(G)| = 29$, torej $K(G)$ vsekakor ni podgrupa $G$. Komutatorska podgrupa je le nekoliko večja, $|[G,G]| = 32$. Primer elementa v $[G,G]$, ki ni hkrati v $K(G)$, je permutacija $(5 \ 6)(7 \ 8)$.

</div>

V luči zgleda je teoriji grup vsekakor v interesu, da bi razumela, kdaj dan element $g \in G$ pripada množici $K(G)$. Lahko smo celo bolj natančni in se vprašamo, na koliko načinov lahko $g$ zapišemo kot komutator. V ta namen predpišimo funkcijo
```{math}
N \colon G \to \NN_0, \quad
    g \mapsto |\{ (x,y) \in G \times G \mid g = [x,y] \}|.
```
Dokazali bomo naslednjo formulo za izračun funkcije $N$ s pomočjo teorije upodobitev.

<div class="izrek">

Naj bo $G$ končna grupa. Za vsak $g \in G$ velja
```{math}
N(g) = |G| \cdot \sum_{\pi \in \Irr(G)} \frac{\chi_{\pi}(g)}{\chi_{\pi}(1)}.
```

</div>

### Harmonična analiza

Funkcijo $N$ obravnavajmo kot element prostora $\fun(G,\CC)$. Ni se težko prepričati, da je $N$ razredna funkcija. Za vsak $z \in G$ namreč velja
```{math}
[z x z^{-1}, z y z^{-1}] = z [x,y] z^{-1},
```
torej vsak par $(x,y)$ z lastnostjo $[x,y] = g$ porodi par $(z x z^{-1}, z y z^{-1})$ z lastnostjo $[z x z^{-1}, z y z^{-1}] = z g z^{-1}$. S tem je $N(g) = N(z g z^{-1})$.

Funkcijo $N$ bomo prepisali v malo bolj nenavadno obliko, ki pa nam bo dobro služila v nadaljevanju. Recimo, da za elementa $x,y \in G$ velja $[x,y] = g$. To enakost interpretiramo kot $x^{-1} \cdot y^{-1} x y = g$, torej je $g$ zapisan kot produkt elementa $x^{-1}$ in elementa, ki je konjugiran $x$. Vsakemu takemu paru $(x,y)$ lahko zato priredimo konjugiranostni razred $\conclass = x^G$ in elementa $a = x^{-1} \in \conclass^{-1}$ ter $b = y^{-1} x y \in \conclass$, za katera velja $a \cdot b = g$. S tem smo opisali prirejanje
```{math}
\psi \colon \{ (x,y) \in G \times G \mid g = [x,y] \} \to 
    \{ (\conclass, a, b) \mid \conclass = (a^{-1})^G, \ b \in \conclass,\ a \cdot b = g \}.
```
To prirejanje *ni* injektivno, saj s trojico $(\conclass,a,b)$ element $y$ ni enolično določen, pač pa le do odseka po centralizatorju $C_G(a^{-1}) = C_G(a)$ natančno.[^11] Torej je $|\psi^{-1}(\conclass,a,b)| = |C_G(a)| = |G|/|\conclass|$. S tem lahko izrazimo
```{math}
N(g) = \sum_{\conclass} \frac{|G|}{|\conclass|} \cdot |\{ (a,b) \in G \times G \mid a \in \conclass^{-1}, \ b \in \conclass, \ a \cdot b = g \}|,
```
kjer vsota teče po vseh konjugiranostnih razredih grupe $G$.

Dobljeni zapis funkcije $N$ je priročen, ker je izražen le s konjugiranostnimi razredi in je neodvisen od izbire njihovih konkretnih predstavnikov. S tem je primeren za gnetenje s Fourierovo transformacijo. Najprej opazimo, da lahko drugi faktor zadnje vsote zapišemo kot
```{math}
\sum_{a,b \in G, \ a \cdot b = g} 1_{\conclass^{-1}}(a) \cdot 1_{\conclass}(b) = \left( 1_{\conclass^{-1}} * 1_{\conclass} \right) (g),
```
zato je
```{math}
N(g) = \sum_{\conclass} \frac{|G|}{|\conclass|} \cdot \left( 1_{\conclass^{-1}} * 1_{\conclass} \right) (g).
```
Konvolucijo lahko po Fourierovi inverziji razvijemo po karakterjih. Ker gre za karakteristične funkcije konjugiranostnih razredov, je ta razvoj še posebej preprost.

<div class="trditev">

Naj bo $G$ končna grupa in $\conclass_1$, $\conclass_2$ konjugiranostna razreda v $G$. Velja
```{math}
1_{\conclass_1} * 1_{\conclass_2} = \frac{|\conclass_1| \cdot |\conclass_2|}{|G|} \sum_{\pi \in \Irr(G)} \frac{\overline{\chi_{\pi}(\conclass_1)} \cdot \overline{\chi_{\pi}(\conclass_2)}}{\chi_{\pi}(1)} \chi_{\pi}.
```

</div>

<div class="dokaz">

Uporabimo Fourierovo inverzijo za funkcijo $1_{\conclass_1} * 1_{\conclass_2}$. Za vsak $g \in G$ dobimo
```{math}
\left( 1_{\conclass_1} * 1_{\conclass_2} \right) (g) 
        = \frac{1}{|G|} \sum_{\pi \in \Irr(G)} \chi_{\pi}(1) \tr \left( \widehat{1_{\conclass_1} * 1_{\conclass_2}}(\pi) \cdot \pi(g) \right).
```
Fourierova transformacija konvolucije je produkt Fourierovih transformacij, ki jih za dani karakteristični funkciji ni težko izračunati po lemi o Fourierovi transformaciji razredne funkcije. Za vsako nerazcepno kompleksno upodobitev $\pi$ na prostoru $V$ velja
```{math}
\widehat{1_{\conclass_1} * 1_{\conclass_2}}(\pi) =
        |\conclass_1| \cdot |\conclass_2| \cdot \frac{\overline{\chi_{\pi}(\conclass_1)} \cdot \overline{\chi_{\pi}(\conclass_2)}}{\chi_{\pi}(1)^2} \cdot {\textstyle \id_V}.
```
Trditev je s tem dokazana.

</div>

Trditev uporabimo za razvoj funkcije $N$ kot
```{math}
N(g) = \sum_{\conclass} \frac{|G|}{|\conclass|} \cdot \frac{|\conclass|^2}{|G|} \sum_{\pi \in \Irr(G)} \frac{|\chi_{\pi}(\conclass)|^2}{\chi_{\pi}(1)} \chi_{\pi}(g)
    = \sum_{\pi \in \Irr(G)} \frac{\chi_{\pi}(g)}{\chi_{\pi}(1)} \sum_{\conclass} |\conclass| \cdot |\chi_{\pi}(\conclass)|^2.
```
Zadnja vsota je ravno enaka $|G| \cdot \langle \chi_{\pi}, \chi_{\pi} \rangle = |G|$, zato nazadnje sklenemo
```{math}
N(g) = |G| \cdot \sum_{\pi \in \Irr(G)} \frac{\chi_{\pi}(g)}{\chi_{\pi}(1)}.
```
S tem smo izpeljali Frobeniusov izrek.

### Prepoznavanje komutatorjev

S Frobeniusovim izrekom lahko komutatorje v grupi prepoznavamo neposredno iz tabele karakterjev grupe.

<div class="posledica">

Naj bo $G$ končna grupa. Za vsak $g \in G$ velja
```{math}
g \in K(G) \quad \Longleftrightarrow \quad \sum_{\pi \in \Irr(G)} \frac{\chi_{\pi}(g)}{\chi_{\pi}(1)} \neq 0.
```

</div>

<div class="zgled">

Naj bo $G = \langle x, y \rangle$ grupa moči $96$ iz zadnjega zgleda. S predstavljenim algoritmom lahko hitro izračunamo njeno tabelo karakterjev. Grupa ima sicer $12$ razredov za konjugiranje, zato je njena tabela karakterjev kar velika.

|               | $()$ | $(5,6)(7,8)$ |   $y$   | $[x,y]$ |    $x$     |
|:-------------:|:------:|:--------------:|:---------:|:---------:|:------------:|
| $\chi_{1}$  | $1$  |     $1$      |   $1$   |   $1$   |    $1$     |
| $\chi_{2}$  | $1$  |     $1$      |   $1$   |   $1$   |  $\zeta$   |
| $\chi_{3}$  | $1$  |     $1$      |   $1$   |   $1$   | $\zeta^2$  |
| $\chi_{4}$  | $3$  |     $3$      |  $-1$   |  $-1$   |    $0$     |
| $\chi_{5}$  | $6$  |     $2$      |   $0$   |   $0$   |    $0$     |
| $\chi_{6}$  | $3$  |     $-1$     |   $1$   | $-1+2i$ |    $0$     |
| $\chi_{7}$  | $3$  |     $-1$     |   $1$   | $-1-2i$ |    $0$     |
| $\chi_{8}$  | $3$  |     $-1$     | $-1+2i$ |   $1$   |    $0$     |
| $\chi_{9}$  | $3$  |     $-1$     | $-1-2i$ |   $1$   |    $0$     |
| $\chi_{10}$ | $2$  |     $-2$     |   $0$   |   $0$   |    $-1$    |
| $\chi_{11}$ | $2$  |     $-2$     |   $0$   |   $0$   | $-\zeta^2$ |
| $\chi_{12}$ | $2$  |     $-2$     |   $0$   |   $0$   |  $-\zeta$  |

Del tabele karakterjev `SmallGroup(96, 3)`, kjer je $\zeta = e^{2 \pi i / 3}$

Iz tabele lahko razberemo, da je element $[x,y]$ res komutator, saj je
```{math}
\sum_{i = 1}^{12} \frac{\chi_i([x,y])}{\chi_i(1)} = 
    3 - \frac13 - 2 \cdot \frac13 + 2 \cdot \frac13 = 
    \frac83 \neq 0.
```
Po drugi strani je element $(5 \ 6)(7 \ 8)$ v jedru vseh linearnih upodobitev, zato pripada komutatorski podgrupi $[G,G]$. Hkrati pa ta element *ne* pripada $K(G)$, saj je
```{math}
\sum_{i = 1}^{12} \frac{\chi_i((5 \ 6)(7 \ 8))}{\chi_i(1)} =
    3 + 1 + \frac13 - 4 \cdot \frac13 - 3 = 0.
```
Njegov konjugiranostni razred v $G$ sestoji iz treh elementov. Ko te elemente dodamo množici $K(G)$, dobimo ravno $[G,G]$.

</div>

<div class="domacanaloga">

Iz tabele karakterjev grupe $\GL_2(\FF_p)$ razberi, da za $p>2$ velja
```{math}
\textstyle K(\GL_2(\FF_p)) = \SL_2(\FF_p).
```
Iz tabele karakterjev grupe $\SL_2(\FF_p)$ razberi, da za $p>3$ množica komutatorjev v $\SL_2(\FF_p)$ vsebuje vse neskalarne elemente. Sklepaj, da je za $p>3$ vsak element grupe $\PSL_2(\FF_p)$ komutator.

</div>

Nedavno razrešena Orejeva domneva iz leta 1951 je predvidevala, da je vsak element nekomutativne končne enostavne grupe komutator. Ta domneva je bila potrjena v [(Liebeck-O’Brien-Shalev-Tiep 2010)](https://ems.press/journals/jems/articles/3979). Dokaz sloni na Frobeniusovi formuli za prepoznavanje komutatorjev. Avtorji z uporabo generičnih tabel karakterjev, Deligne-Lusztigove teorije in kar nekaj surove računske moči dokažejo, da prispevki nelinearnih karakterjev v Frobeniusovi formuli nikdar ne uspejo izničiti prispevka trivialnega karakterja.

Velika sestra Orejeve domneve je Thompsonova domneva.

<div class="odprtproblem">

V vsaki nekomutativni končni enostavni grupi $G$ obstaja konjugiranostni razred $\conclass$, da je $G = \conclass \cdot \conclass$.

</div>

Thompsonova domneva implicira Orejevo domnevo. Če namreč najdemo tak konjugiranostni razred $\conclass$, potem je v posebnem $1 \in \conclass \cdot \conclass$, zato je $\conclass = \conclass^{-1}$. Torej lahko vsak element $g \in G$ zapišemo kot $g = x^{-1} x^{g_2}$ za nek $x \in \conclass$, s čimer je $g = [x, g_2]$. Ker je bil $g$ poljuben, je torej vsak element v $G$ komutator, kar je ravno trditev Orejeve domneve.

Ta močnejša domneva je še vedno nerazrešena, je pa v zadnjih letih bilo kar nekaj aktivnosti v zvezi z njeno asimptotsko veljavnostjo. Ti rezultati večinoma temeljijo na teoriji karakterjev na naslednji način. Element $g \in G$ pripada $\conclass \cdot \conclass$, če in samo če velja $(1_{\conclass} * 1_{\conclass})(g) \neq 0$, kar lahko s pomočjo Fourierove inverzije, kot smo videli v zadnji trditvi, zapišemo kot
```{math}
\sum_{\pi \in \Irr(G)} \frac{\overline{\chi_{\pi}(\conclass)}^2}{\chi_{\pi}(1)} \chi_{\pi}(g) \neq 0.
```
S pomočjo poznavanja karakterjev končnih enostavnih grup je domneva znana za mnogo primerov, odprtih pa je še nekaj neskončnih družin matričnih grup nad majhnimi polji, kot je zelo prijazno razloženo v Larsenovem predavanju [tukaj](https://www.youtube.com/watch?v=OQFFYaCYzq4).

## Slučajni sprehodi

Naj bo $G$ končna grupa in $S$ neka njena podmnožica, ki generira $G$. Vsak element v $G$ lahko torej zapišemo kot produkt elementov iz množice $S$. V tem razdelku bomo raziskali, kaj se zgodi, če elementov iz množice $S$ ne množimo s ciljem, da bi zapisali nek konkreten element, ampak jih namesto tega množimo kar naključno.

### Slučajni sprehod

Naj bo $G$ grupa z generirajočo množico $S$. Enakomerno naključno izberimo element $X_1 = s_1 \in S$. Za tem še enkrat neodvisno izberimo $s_2 \in S$ in izračunajmo $X_2 = s_1 s_2 \in G$. Ta postopek ponavljamo. Ko že imamo $X_i \in G$, enakomerno naključno izberemo element $s_{i+1} \in S$ in izračunamo $X_{i+1} = X_i s_{i+1}$. Če smo torej po nekaj korakih že prišli do elementa $g \in G$, potem je verjetnost, da bomo po naslednjem koraku v elementu $h \in G$, enaka
```{math}
p_S(g, h)
    = \begin{cases}
        1/|S| & \exists s \in S \colon h = g s, \\
        0 & \text{sicer}
    \end{cases}
```
Po $n$ korakih tega postopka dobimo element $X_n \in G$, ki je seveda odvisen od izbire vmesnih elementov $s_i \in S$ na vsakem koraku. Temu procesu pravimo <span class="definicija">slučajni sprehod</span> na grupi $G$ z generirajočo množico $S$.

<div class="zgled">

Naj bo $G = S_n$ in $S$ množica transpozicij v $S_n$. Predstavljajmo si, da imamo pred sabo urejen kup kart. Enakomerno naključno izberemo dve različni karti v tem kupu, eno z levo roko in eno z desno, in ju zamenjamo. Ta postopek ponovimo $n$-krat. Menjava na vsakem koraku ustreza izbiri naključne transpozicije $\sigma \in S$, s katero pomnožimo trenutno permutacijo, ki opisuje stanje, v katerem je kup kart. Slučajni sprehod v tem primeru torej opisuje slučajno mešanje kupa kart.

</div>

Nekoliko bolj abstraktno bi lahko na slučajni sprehod gledali kot na zaporedje slučajnih spremenljivk $X_1, X_2, \dots$ z vrednostmi v $G$, ki pa niso porazdeljene neodvisno, temveč zanje velja <span class="definicija">lastnost Markova</span>, to je
```{math}
\PP( X_{i+1} = y \mid X_1 = x_1, \dots, X_i = x_i)
    = p_S(x_i, y)
```
za vsak $i \geq 0$ in za vse $x_1, x_2, \dots, x_i \in G$. Ta lastnost je jasno izpolnjena za slučajni sprehod, kot smo ga opisali zgoraj. Po drugi strani je vsako zaporedje slučajnih spremenljivk z vrednostmi v $G$, ki zadošča lastnosti Markova, *uresničljivo* kot slučajni sprehod. Definiciji sta torej ekvivalentni.

Slučajna spremenljivka $X_n$ nam pove, v katerem elementu se nahajamo po $n$ korakih slučajnega sprehoda. Naš cilj je analizirati porazdelitev te slučajne spremenljivke v odvisnosti od $n$ in še posebej v limiti, ko gre $n$ čez vse meje. Kot bomo videli, je tudi ta problem izrazljiv v jeziku teorije upodobitev.

### Operator Markova

Po $n$ korakih slučajnega sprehoda se znajdemo v nedoločenem elementu grupe $G$. Uvedimo funkcijo
```{math}
\mu_n \colon G \to \CC, \quad
    g \mapsto \PP(X_n = g),
```
ki meri verjetnost, da smo v danem elementu. Ta funkcija torej ni nič drugega kot porazdelitvena funkcija slučajne spremenljivke $X_n$. Slučajni sprehod se prične v $1$, zato je $\mu_0 = 1_1$.

Vrednosti funkcije $\mu_n$ lahko izračunamo induktivno na $n$, upoštevajoč lastnost Markova. Velja
```{math}
\mu_n(g) 
    = \sum_{h \in G} \PP(X_n = g \mid X_{n-1} = h) \PP(X_{n-1} = h)
    = \sum_{h \in G} p_{S}(h,g) \cdot \mu_{n-1}(h).
```
Vrednosti $p_{S}(h,g)$ so neničelne le, kadar je $g \in h S$. Dobimo torej
```{math}
\mu_n(g)
    = \frac{1}{|S|} \sum_{h \in g S^{-1}} \mu_{n-1}(h)
    = \frac{1}{|S|} \sum_{x \in G} \mu_{n-1}(gx^{-1}) 1_{S}(x),
```
Zadnjo vsoto prepoznamo kot konvolucijo
```{math}
\left( \mu_{n-1} * \frac{1_{S}}{|S|} \right) (g),
```
ki jo lahko zapišemo s pomočjo Fourierove transformacije in nazadnje dobimo
```{math}
\mu_n = \widehat{\frac{1_{S}}{|S|} }(\rho_{\fun}) \cdot \mu_{n-1}.
```
Rekurzivna zveza za izračun porazdelitvene funkcije $\mu_n$ iz $\mu_{n-1}$ se torej izrazi s pomočjo Fourierove transformacije normalizirane karakteristične funkcije generirajoče množice $S$ v regularni upodobitvi. Tej linearni preslikavi pravimo <span class="definicija">operator Markova</span> in jo označimo kot
```{math}
M = \widehat{\frac{1_{S}}{|S|} }(\rho_{\fun}) = \frac{1}{|S|} \sum_{x \in S} \rho_{\fun}(x)^*.
```
Za poljubno funkcijo $f \in \fun(G,\CC)$ je
```{math}
(M \cdot f)(g) = \frac{1}{|S|} \sum_{x \in S} f(g x^{-1}),
```
torej $Mf$ v točki $g \in G$ izračuna povprečje funkcije $f$ po vseh elementih, ki v slučajnem sprehodu lahko vodijo v $g$.

<div class="trditev">

Za slučajni sprehod na grupi z operatorjem Markova $M$ je
```{math}
\mu_n = M^n \cdot 1_1.
```

</div>

Operator Markova lahko zapišemo v naravni bazi karakterističnih funkcij in s tem dobimo matriko razsežnosti $|G| \times |G|$, ki ima v vsakem stolpcu $|S|$ neničelnih vrednosti, vsaka od njih je enaka $1/|S|$. Ob dodatnih predpostavkah na množico $S$ dobimo dodatne lastnosti te matrike. Če je na primer množica $S$ simetrična, kar pomeni, da je za vsak $s \in S$ tudi $s^{-1} \in S$, potem je opisana matrika za $M$ *simetrična* in zato nujno *diagonalizabilna* v ortonormirani bazi nad realnimi števili. V tem primeru ni težko izračunati visokih potenc $M$ in s tem $\mu_n$.

<div class="zgled">

Opazujmo simetrično grupo $S_3$ z generirajočo množico transpozicij $S = \{ (1 \ 2), (1 \ 3), (2 \ 3)\}$. Ta množica je simetrična. Elemente grupe $S_3$ uredimo po vrsti kot
```{math}
(),
    (1 \ 2),
    (1 \ 3),
    (2 \ 3),
    (1 \ 2 \ 3),
    (1 \ 3 \ 2).
```
Operator Markova je v standardni bazi karakterističnih funkcij elementov grupe enak
```{math}
M = \frac13 \begin{pmatrix}
        0 & 1 & 1 & 1 & 0 & 0 \\
        1 & 0 & 0 & 0 & 1 & 1 \\
        1 & 0 & 0 & 0 & 1 & 1 \\
        1 & 0 & 0 & 0 & 1 & 1 \\
        0 & 1 & 1 & 1 & 0 & 0 \\
        0 & 1 & 1 & 1 & 0 & 0 \\
    \end{pmatrix}.
```
Ta matrika je simetrična. Njen karakteristični polinom je enak $\lambda^6 - \lambda^4$, zato dobimo lastne vrednosti $(1,0,0,0,0,-1)$. Lastni vektor lastne vrednosti $1$ je konstantni vektor $1$, ki ustreza konstantni funkciji na $S_3$. Lastni vektor lastne vrednosti $-1$ je vektor $\sgn$. Funkcijo $1_1$ razvijemo po lastnih vektorjih kot
```{math}
1_1 = 
    \left\langle 1_1, 1 \right\rangle +
    \left\langle 1_1, \sgn \right\rangle \sgn +
    k,
```
kjer je $k \in \ker M$. Velja torej
```{math}
1_1 =
    \frac{1}{6} + \frac{1}{6} \sgn + k.
```
Za vsak $n$ s tem dobimo
```{math}
\mu_n = M^n \cdot 1_1 = \frac{1}{6} + \frac{(-1)^n}{6} \cdot \sgn
    = \begin{cases}
        \frac{1}{3} \cdot 1_{A_3} & n \equiv 0 \pmod{2}, \\
        \frac{1}{3} \cdot 1_{S_3 \backslash A_3} & n \equiv 1 \pmod{2}.
    \end{cases}
```
Porazdelitev po sodo mnogo korakih je torej enakomerna na sodih permutacijah $A_3$, po liho mnogo korakih pa enakomerna na lihih permutacijah $S_3 \backslash A_3$.

</div>

Enakomerno porazdelitev na množici $A \subseteq G$ označimo z $U_A$. Velja $U_A = 1/|A| \cdot 1_A$. Enakomerna porazdelitev $U_G$ je vselej lastni vektor operatorja Markova z lastno vrednostjo $1$. Preostalih lastnih vrednosti pa v splošnem ni lahko določiti.

<div class="domacanaloga">

Naj bo $G$ končna grupa z generirajočo množico $S$ in operatorjem Markova $M$. Dokaži, da za vsako funkcijo $f \in \fun(G,\CC)$ velja $||Mf|| \leq ||f||$. Sklepaj, da so vse lastne vrednosti $M$ po absolutni vrednosti kvečjemu $1$. Kaj je lastni vektor za lastno vrednost $1$? Kdaj je $-1$ lastna vrednost in kaj je pripadajoči lastni vektor?

</div>

<div class="domacanaloga">

Naj bo $p$ praštevilo in $S \subseteq \FF_p$. Za vsak $i \in \FF_p$ naj bo $R_i$ število rešitev enačbe $x_1 + x_2 + \cdots + x_p = i$, kjer so vse spremenljivke v $S$. Dokaži, da je $R_i / |S|^p = \mu_p(i)$, kjer je $\mu_p$ porazdelitvena funkcija slučajnega sprehoda v grupi $\FF_p$ z množico $S$. Sklepaj, da je $R_0 \equiv |S| \pmod{p}$ in $R_i \equiv 0 \pmod{p}$ za $i \neq 0$.[^12]

</div>

### Slučajni sprehod s konjugiranostnim razredom

Zelo dobro razumemo primer, ko je $S$ konjugiranostni razred v $G$, saj lahko Fourierovo transformacijo razredne funkcije eksplicitno izračunamo v odvisnosti od karakterjev. V tem primeru lahko eksplicitno določimo tudi vse lastne vektorje, ki jih dobimo kot generatorje izotipičnih komponent nerazcepnih upodobitev, ko smo videli v predstavljenem algoritmu za izračun tabele karakterjev.

<div class="trditev">

Za slučajni sprehod na grupi $G$ z generirajočo množico $\conclass$, kjer je $\conclass$ konjugiranostni razred v $G$, je operator Markova diagonalizabilen z lastnimi vrednostmi
```{math}
r_{\pi}(\conclass) = \frac{\overline{\chi_{\pi}(\conclass)}}{\chi_{\pi}(1)}
```
za vsako nerazcepno kompleksno upodobitev $\pi \in \Irr(G)$, pri čemer je večkratnost vsake lastne vrednosti enaka $\chi_{\pi}(1)^2$.

</div>

Operator Markova $M$ slučajnega sprehoda na $G$ z generirajočo množico $\conclass$, kjer je $\conclass$ konjugiranostni razred v $G$, deluje na vsaki od izotipičnih komponent regularne upodobitve kot skalarni večkratnik identitete z znamimi skalarji. Da lahko razumemo $\mu_n = M^n \cdot 1_1$, moramo najprej razviti funkcijo $1_1$ po izotipičnih komponentah. To naredimo, kot smo že, s pomočjo Fourierovih transformacij nerazcepnih karakterjev. Projekcija $1_1$ na $\pi$-izotipično komponento je enaka
```{math}
v_{\pi} = \frac{\chi_{\pi}(1)}{|G|} \cdot \chi_{\pi},
```
zato dobimo $1_1 = \sum_{\pi \in \Irr(G)} v_{\pi}$. Vektor $v_{\pi}$ je lastni vektor za $M$ z lastno vrednostjo $r_{\pi}(\conclass)$. V tej množici lastnih vektorjev lahko torej funkcijo $\mu_n$ razvijemo kot
```{math}
\mu_n = M^n \cdot 1_1 = \sum_{\pi \in \Irr(G)} r_{\pi}(\conclass)^n \cdot v_{\pi}.
```
Za razumevanje asimptotskega obnašanja $\mu_n$ je pomembno poznati $|r_{\pi}(\conclass)|$. Če je namreč $|r_{\pi}(\conclass)| < 1$, potem vrednosti $r_{\pi}(\conclass)^n$ konvergirajo k $0$, ko gre $n$ čez vse meje.

<div class="lema">

Za $\pi \in \Irr(G)$ drži $|r_{\pi}(\conclass)| \leq 1$, pri čemer velja enakost natanko tedaj, ko je
```{math}
\{ [g,c] \mid g \in G, c \in \conclass \} \subseteq \ker \pi.
```

</div>

<div class="dokaz">

Naj bo $x \in \conclass$. Enakost $|r_{\pi}(x)| = 1$ velja natanko tedaj, ko je $\pi(x)$ skalarna matrika. Taka matrika komutira z vsemi elementi $\pi(g)$ za $g \in G$. Velja torej $\pi([g, \conclass]) = 1$ za vsak $g \in G$. To pomeni, da je $[G, \conclass] \subseteq \ker \pi$, kar je enakovredno vsebovanosti v trditvi. Premislimo še, da za matriko $A$ velja $[A, \pi(g)] = 1$ za vse $g \in G$, če in samo če je $A$ skalarna matrika. Vektorski prostor, ki ga razpenjajo matrike $\pi(g)$ za $g \in G$, je enak prostoru matrik $M_{\deg(\pi)}(\CC)$,[^13] v tej algebri pa so centralne matrike ravno skalarne matrike. Dokaz je s tem zaključen.

</div>

Zberimo prispevke z maksimalno vrednostjo $r_{\pi}(\conclass)$ v množico
```{math}
X_{\conclass} = \{ \pi \in \Irr(G) \mid |r_{\pi}(\conclass)| = 1 \}.
```
Velja torej
```{math}
\mu_n - \sum_{\pi \in X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi}
    = \sum_{\pi \in \Irr(G) \backslash X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi}.
```
Prispevki $r_{\pi}(\conclass)^n$ za $\pi$ izven $X_{\conclass}$ konvergirajo k $0$ za velike vrednosti $n$ in zatorej dobimo
```{math}
\lim_{n \to \infty} \left( \mu_n - \sum_{\pi \in X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi} \right) = 0.
```
Za konkretne grupe lahko s tabelo karakterjev ali upoštevanjem kakšnih dodatnih lastnosti eksplicitno izračunamo zadnjo vsoto in s tem določimo limitno porazdelitev $\mu_n$, če ta sploh obstaja.

<div class="domacanaloga">

Naj bo $G$ nekomutativna končna enostavna grupa. Dokaži, da vsak netrivialen konjugiranostni razred $\conclass$ generira $G$ in da velja $X_{\conclass} = \{ \oneone \}$. Sklepaj, da je $\lim_{n \to \infty} \mu_n = U_G$.

</div>

Napako pri aproksimaciji porazdelitev $\mu_n$ in vsoto prispevkov po $X_{\conclass}$ izrazimo s pomočjo norme $||f||_1 = \sum_{g \in G} |f(g)|$ za funkcijo $f \in \fun(G,\CC)$.[^14] Naj bo $0 < \theta < 1$ konstanta. <span class="definicija">Čas mešanja</span>[^15] $t_{mix}(\theta)$ je najmanjše število $n$, pri katerem je
```{math}
|| \mu_n -  \sum_{\pi \in X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi} ||_1  \leq \theta.
```
Čas mešanja in s tem hitrost konvergence k limitni porazdelitvi lahko kvantitativno nadziramo, če dobro poznamo vrednosti $r_{\pi}(\conclass)$ za $\pi$ izven $X_{\conclass}$, saj velja
```{math}
|| \mu_n -  \sum_{\pi \in X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi} ||_1
    \leq
    \sum_{\pi \in \Irr(G) \backslash X_{\conclass}} |r_{\pi}(\conclass)|^n \cdot ||v_{\pi}||_1.
```
Normo baznih vektorjev $v_{\pi}$ lahko omejimo s Cauchy-Schwartzovo neenakostjo kot
```{math}
||v_{\pi}||_1 = \frac{\chi_{\pi}(1)}{|G|} \sum_{g \in G} |\chi_{\pi}(g)|
    \leq \frac{\chi_{\pi}(1)}{|G|} \sqrt{|G| \cdot \sum_{g \in G} |\chi_{\pi}(g)|^2}
    = \chi_{\pi}(1).
```
S tem velja
```{math}
|| \mu_n -  \sum_{\pi \in X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi} ||_1
    \leq \left( \max_{\pi \in \Irr(G) \backslash X_{\conclass}} |r_{\pi}(\conclass)| \right)^n  \cdot \sum_{\pi \in \Irr(G) \backslash X_{\conclass}} \chi_{\pi}(1).
```
Če vsoto karakterjev zelo grobo navzgor ocenimo z $|G|$ in upoštevamo, da je
```{math}
\max_{\pi \in \Irr(G) \backslash X_{\conclass}} |r_{\pi}(\conclass)|  \leq 1 - \epsilon < 1
```
za nek $\epsilon > 0$, potem velja
```{math}
|| \mu_n -  \sum_{\pi \in X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi} ||_1
    \leq (1 - \epsilon)^n \cdot |G|.
```

Napaka med porazdelitvama pade pod konstanto $\theta$, če je le
```{math}
n \sim (\log |G| - \log \theta)/(- \log (1 - \epsilon)) = O_{\epsilon, \theta}(\log |G|).
```
Takrat bo za majhno konstanto $\theta$ slučajni sprehod zelo blizu svoje limitne porazdelitve, če ta sploh obstaja. Čas mešanja je torej logaritmičen v velikosti grupe.

### Naključno množenje podobnih matrik

Oglejmo si konkreten primer slučajnega sprehoda. Obravnavajmo grupo $G_p = \GL_2(\FF_p)$ za $p > 3$, ki smo jo že dodobra spoznali. V njej za generirajočo množico izberimo konjugiranostni razred $\conclass$ regularnih polenostavnih elementov, ki so podobni matriki
```{math}
A = \begin{pmatrix}
        \delta & 0 \\ 0 & 1 
    \end{pmatrix},
```
kjer je $\delta$ generator ciklične grupe obrnljivih elementov končnega polja $\FF_p^*$. Generirajoča množica sestoji torej iz vseh matrik, ki so v $G_p$ podobne $A$.

#### Generiranje grupe

Preverimo najprej, da množica $\conclass$ res generira $G_p$. Ker je $G_p$ končna grupa, velja $A^{-1} \in \langle \conclass \rangle$ in zato je vsaka matrika, ki je podobna $A^{-1}$, tudi v $\langle \conclass \rangle$. S tem velja
```{math}
[S_+, A] = (S_+^{-1} A^{-1} S_+) A  = S_+^{\delta^{-1} - 1}
    \in \langle \conclass \rangle.
```
Ker je $p > 3$, je $\delta \neq \pm 1$, zato dobimo $S_+ \in \langle \conclass \rangle$. Sorodno sklepamo za matriko $S_-$. S tem dobimo
```{math}
\textstyle \langle \conclass \rangle \geq \langle S_+, S_- \rangle = \SL_2(\FF_p).
```
Ker je $\delta$ generator $\FF_p^*$, grupa $\langle \conclass \rangle$ vsebuje matrike z vsemi možnimi determinantami. Od tod sledi, da $\conclass$ res generira grupo $G_p$.

#### Limitna porazdelitev sprehoda

Za razumevanje limitnega obnašanja porazdelitve $\mu_n$ moramo najprej določiti vrednosti $r_{\pi}(\conclass)$. Tabelo karakterjev grupe $G_p$ v celoti poznamo.

|  | $\chi_{\pi}(1)$ | $\overline{\chi_{\pi}(\conclass)}$ | $r_{\pi}(\conclass)$ | $\abs{r_{\pi}(\conclass)}$ |  |
|:---|:--:|:--:|:--:|:--:|:--:|
| $\chi \circ \det$ | $1$ | $\overline{\chi(\delta)}$ | $\overline{\chi(\delta)}$ | $1$ |  |
| $\St(\chi)$ | $p$ | $\overline{\chi(\delta)}$ | $\overline{\chi(\delta)} / p$ | $1/p$ |  |
| $\pi(\chi_1, \chi_2)$ | $p+1$ | $\overline{\chi_1(\delta)} + \overline{\chi_2(\delta)}$ | $(\overline{\chi_1(\delta)} + \overline{\chi_2(\delta)})/(p+1)$ | $< 2/(p+1)$ |  |
| $\zeta_{\theta}$ | $p-1$ | $0$ | $0$ | $0$ |  |

Lastne vrednosti operatorja Markova grupe $G_p$ z generirajočo množico $\conclass$

Množica $X_{\conclass}$ v tem primeru sestoji iz linearnih upodobitev. Vsota prispevkov porazdelitev po $X_{\conclass}$ je zato enaka
```{math}
\sum_{\pi \in X_{\conclass}} r_{\pi}(\conclass)^n \cdot v_{\pi}
    = \sum_{\chi \in \Irr(\FF_p^*)} \overline{\chi(\delta^{n})} \cdot \frac{1}{|G_p|} \chi \circ \det.
```
Upoštevamo drugo ortogonalnostno relacijo in dobimo
```{math}
\frac{1}{|G_p|} \cdot \left( g \mapsto \begin{cases}
        |\FF_p^*| & \det g = \delta^n \\
        0 & \text{sicer.}
    \end{cases}
    \right)    
    = \frac{1}{|\SL_2(\FF_p)|} \cdot 1_{\det^{-1}(\delta^n)}
    = U_{\det^{-1}(\delta^n)}.
```
V tem primeru kandidat za limitno porazdelitev v resnici ne konvergira, saj za različne vrednosti $n$ po modulu $p-1$ dobimo bistveno različne porazdelitve. Ko je $n$ deljiv s $p-1$, dobimo enakomerno porazdelitev na $\SL_2(\FF_p)$.

#### Hitrost konvergence

Pogovorimo se še o oceni napake pri aproksimaciji $\mu_n$ s kandidatom za limitno porazdelitev. Za $\pi$ izven $X_{\conclass}$ ocenimo
```{math}
\max_{\pi \in \Irr(G_p) \backslash X_{\conclass}} |r_{\pi}(\conclass)| < \frac{2}{p}, \quad
    \sum_{\pi \in \Irr(G_p) \backslash X_{\conclass}} \chi_{\pi}(1)
    < p^3.
```
Velja torej
```{math}
|| \mu_n - U_{\det^{-1}(\rho^n)} ||_1
    \leq
    \frac{2^n}{p^{n-3}}.
```
Napaka zelo hitro upade, pod $\theta$ je že pri $n = (3 \log p - \log \theta) / (\log p - \log 2) \sim 3$.[^16] Težava je le ta, da $\mu_n$ v resnici ne konvergira. Da to popravimo, moramo opazovati obnašanje po aritmetičnih zaporedjih z razliko $p-1$. Za vse dovolj velike $p$ tako dobimo zelo dobro aproksimacijo
```{math}
\mu_{p-1} \approx U_{\SL_2(\FF_p)}.
```
Če torej v $G_p$ naključno zmnožimo $p-1$ matrik v $\conclass$ za dovolj velik $p$, dobimo (skoraj) naključno matriko v $\SL_2(\FF_p)$. Napaka sicer pade ekstremno hitro, a linearni karakterji obremenijo sprehod do te mere, da ne moremo izkoristiti majhne napake že po $3$ korakih, niti ne po $\log |G_p| \sim \log p$ korakih, temveč šele po $p-1 \sim |G_p|^{1/4}$ korakih.

<div class="domacanaloga">

Obravnavaj slučajni sprehod v $\PSL_2(\FF_p)$ glede na nek konjugiranostni razred $\conclass$. V tem primeru bo $\lim_{n \to \infty} \mu_n$ enakomerna porazdelitev na $\PSL_2(\FF_p)$. S pomočjo tabele karakterjev oceni hitrost konvergence in pokaži, da dosežemo približno naključno matriko v $\PSL_2(\FF_p)$ mnogo hitreje kot po $p-1$ korakih.

</div>

<div class="domacanaloga">

Obravnavaj slučajni sprehod v $S_n$ glede na generirajočo množico $S$, ki sestoji iz transpozicij in enote $()$. To ni konjugiranostni razred, je pa unija dveh razredov. Premisli, kako lahko argumente posplošiš na to situacijo. Določi limitno porazdelitev. Ocena hitrosti konvergence bo zahtevala kar nekaj truda. Pomagaš si lahko z [(Miščič 2022)](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=139856&lang=eng).

</div>

### Konvergenca v družinah

Za vsako konkretno nekomutativno končno enostavno grupo $G$ jasno velja, da so vse lastne vrednosti operatorja $M$ razen $1$ po absolutni vrednosti kvečjemu $1-\epsilon$ za nek $\epsilon = \epsilon(G) > 0$. V tem primeru rečemo, da je grupa $G$ <span class="definicija">$\epsilon$-ekspanzivna</span> glede na generirajočo množico $S$. Slučajni sprehod v taki grupi se dobro premeša po $O_{\epsilon}(\log |G|)$ korakih. Težave nastopijo, ko skušamo ta argument uporabiti za celo družino grup, saj se lahko zgodi, da z večanjem parametra $n$ vrednost ekspanzivnosti $\epsilon = \epsilon_n$ nujno konvergira k $0$. Ta fenomen vidimo v primeru družine $A_n$ in konjugiranostnega razreda $3$-ciklov.

<div class="domacanaloga">

Obravnavaj slučajni sprehod v $A_n$ glede na konjugiranostni razred $3$-ciklov $\conclass$. Premisli, da je $\max_{\oneone \neq \pi \in \Irr(A_n)} |r_{\pi}(\conclass)| = 1 - 3/(n-1)$ in s tem oceni hitrost konvergence.

</div>

V taki situaciji se slučajni sprehodi zmešajo dobro po $O_{\epsilon}(\log |G|)$ korakih, kar je lahko bistveno večje od $O(\log |G|)$ in torej asimptotsko gledano v resnici ni logaritmično v velikosti grupe.

Družini grup $(G_i, S_i)_{i \in \NN}$, kjer je $G_i = \langle S_i \rangle$, pravimo <span class="definicija">ekspanzivna družina</span>,[^17] kadar obstaja konstanta $\epsilon > 0$, za katero je vsaka grupa $G_i$ $\epsilon$-ekspanzivna glede na $S_i$. V ekspanzivnih družinah se slučajni sprehodi enakomerno zelo hitro dobro premešajo.

Vsaka družina je ekspanzivna, če za generatorsko množico vzamemo kar $S_i = G_i$ za vsak $i$. V tem primeru je namreč operator Markova enak povprečju $\EE(\rho_{\fun})$, ki je projektor na trivialno podupodobitev regularne, zato so vse njegove netrivialne lastne vrednosti ničelne. Želimo si ekspanzivnih družin, v katerih je množica $S_i$ čim manjša, po možnosti celo omejene velikosti v vseh članicah družine, na primer $|S_i| \leq 100$ za vsak $i$. V takih ekspanzivnih družinah lahko enakomerno zelo hitro z zaporednim vzorčenjem v množici omejene velikosti dobimo približno enakomerno naključne elemente ogromnih grup.

S pomočjo teorije upodobitev in poznavanja določenih lastnosti karakterjev končnih enostavnih grup $\PSL_n(\FF_p)$ ni pretežko posplošiti zgleda iz zadnjega razdelka.[^18] Zanimivo je, da isti rezultat ne deluje za družino alternirajočih grup.

<div class="izrek">

Naj bo $n \geq 2$ fiksno naravno število. Za vsak $p \in \PP$ naj bo $\conclass_{n,p}$ netrivialen konjugiranostni razred v $\PSL_n(\FF_p)$. Tedaj je družina grup $( \PSL_n(\FF_p), \conclass_{n,p} )_{p \in \PP}$ ekspanzivna.

</div>

Bistveno bolj netrivialen pa je dokaz naslednjega izreka, po katerem lahko vse nekomutativne končne enostavne grupe napravimo za ekspanzivne z generatorskimi množicami omejene velikosti.

<div class="izrek">

Obstaja konstanta $C > 0$, tako da je družina nekomutativnih končnih enostavnih grup ekspanzivna družina glede na generatorske množice velikosti kvečjemu $C$.

</div>

Izrek nam zagotavlja obstoj neke ne prevelike generirajoče množice v končnih enostavnih grupah, glede na katere se slučajni sprehodi enakomerno zelo hitro dobro premešajo. Še težje pa je povedati kaj bolj konkretnega o teh generirajočih množicah. Za primer $A_n$ so te množice konstruirane v [(Kassabov 2007)](https://link.springer.com/article/10.1007/s00222-007-0065-y) s pomočjo neke naključne metode. Dokaz omejitev absolutnih vrednosti lastnih vrednosti operatorja Markova sloni na teoriji upodobitev, a je precej bolj zahteven od tega, ki smo si ga ogledali mi, saj so te generatorske množice daleč od konjugiranostnih razredov. Pred nedavnim so se našle celo eksplicitne konstrukcije generirajočih množic $A_n$, glede na katere dobimo ekspanzivno družino [(Caprace-Kassabov 2022)](https://arxiv.org/abs/2210.00730). Tudi tukaj je ključna teorija upodobitev, a v igro vstopijo neskončne grupe avtomorfizmov polinomskih kolobarjev nad končnim poljem.

Dokazi ekspanzivnosti za generatorske množice, ki niso konjugiranostni razredi, ponavadi potekajo na obraten način, kot bi pričakovali. Omejenost absolutnih vrednosti netrivialnih lastnih vrednosti operatorja Markova namreč lahko dokažemo, če premislimo, da se slučajni sprehodi enakomerno zelo hitro premešajo.[^19] Primer uporabe te tehnike par excellence je naslednji rezultat, ki med drugim presenetljivo sloni na Gowersovem rezultatu o zgornji meji gostote množic brez produktov.

<div class="izrek">

Naj bo $n$ *fiksno* naravno število. Za vsak $p \in \PP$ naj bo enakomerno naključno izberemo dva elementa $x,y \in \PSL_n(\FF_p)$ in tvorimo množico $S_{n,p,x,y} = \{ x, x^{-1}, y, y^{-1} \}$. Tedaj obstaja $\epsilon = \epsilon(n)$, da je
```{math}
\lim_{p \to \infty} \PP_{x,y}(\textstyle \text{$\PSL_n(\FF_p)$ je $\epsilon$-ekspanzivna glede na $S_{n,p,x,y}$}) = 1.
```

</div>

Če sprostimo $n$ in opazujemo matrike velikih razsežnosti, cel kup tehnik v dokazu propade. Za te matrike ni znano in med strokovnjaki niti ni jasnega konsenza, ali so asimptotsko gledano skoraj gotovo ekspanzivne. Preprost primer, ki bi verjetno odprl vrata v velike matrike, je družina alternirajočih grup.

<div class="odprtproblem">

V vsaki alternirajoči grupi $A_n$ enakomerno naključno izberemo dva elementa $x,y \in A_n$ in tvorimo množico $S_{n,x,y} = \{ x, x^{-1}, y, y^{-1} \}$. Ali obstaja absolutna konstanta $\epsilon > 0$, da je
```{math}
\lim_{n \to \infty} \PP_{x,y}(\text{$A_n$ je $\epsilon$-ekspanzivna glede na $S_{n,x,y}$}) = 1 ?
```

</div>

Vzpodbuden delni rezultat je, da asimptotska visoko verjetna ekspanzivnost drži za družino določenih *kvocientov Cayleyjevih grafov* simetričnih grup, kot je predstavljeno v [(Milanez 2022)](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=140303). Ti rezultati so bili nedavno posplošeni do *precej velikih* kvocientov Cayleyjevih grafov v [(Cassidy 2025).](https://arxiv.org/abs/2412.13941)

[^1]: Na ta način torej izbiramo aritmetična zaporedja v $\FF_p$ dolžine $3$.

[^2]: Ne bomo preveč natančni glede iteracije. V grobem lahko iz aritmetičnega zaporedja $P_i$ preidemo na ciklično grupo enake moči (morda ne več praštevilske) in potem ponovimo argument v tej ciklični grupi.

[^3]: Glej [(Peluse 2022)](https://arxiv.org/pdf/2206.10037.pdf).

[^4]: Iskanje optimalnih restrikcij na gostoto je predstavljeno v [(Bone 2024)](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=155586&lang=slv).

[^5]: Lahko bi naredili sicer enak razmislek kot v dokazu Rothovega izreka, a nam od tiste točke, ko harmonična analiza odpove, obstoj aritmetičnih zaporedij $P_i$ ne bi koristil za reševanje enačbe $x+y=z$.

[^6]: Za funkciji $f, g \colon \NN \to \RR$ pišemo $f \ll g$, če obstaja konstanta $C$, da je $f(n) \leq C g(n)$ za vse $n$. V primeru, ko za funkciji $f,g$ velja hkrati $f \ll g$ in $g \ll f$, pišemo $f = \Theta(g)$. Funkciji $f$ in $g$ sta torej asimptotsko do konstante natančno enaki.

[^7]: Del tega si bomo ogledali nekoliko kasneje.

[^8]: Za funkciji $f, g \colon \NN \to \RR$ pišemo $f = O(g)$, če velja $f \ll g$, ter $f = o(g)$, če velja $\lim_{n \to \infty} f(n)/g(n) = 0$.

[^9]: Definicija množice $S$ je enaka kot za primer $A_n$, dodaten trud je potreben le za oceno njene gostote.

[^10]: Natančneje, obstajata dve taki neizomorfni grupi.

[^11]: Velja namreč zveza $b = y^{-1} a^{-1} y$.

[^12]: S tem si le slučajni korak stran od rešitve [naloge I/3](https://www.imc-math.org.uk/imc2022/imc2022day1questions.pdf) s tekmovanja IMC 2022.

[^13]: Če namreč ne razpenjajo celotnega prostora matrik, potem obstaja neka netrivialna linearna kombinacija matričnih koeficientov $\{ f_{i,j} \mid 1 \leq i, j \leq \deg(\pi) \}$, ki je v vseh elementih $g \in G$ ničelna. To je protislovje z linearno neodvisnostjo matričnih koeficientov nerazcepne upodobitve $\pi$.

[^14]: Za primerjavo porazdelitev ne uporabljamo standardne norme $||f|| = \langle f, f \rangle^{1/2}$, ampak normo $||f||_1$. Razlog za to je naslednji. Opazujmo družino simetričnih grup $S_n$. Potem je $||U_{A_n} - U_{S_n}||^2 = 1/|S_n|$, kar konvergira k $0$ za $n \to \infty$, čeprav sta porazdelitvi očitno različni. Norma $||\cdot||_1$ nima te pomanjkljivosti; velja $||U_{A_n} - U_{S_n}||_1 = 1$.

[^15]: Rečemo tudi, da se slučajni sprehod <span class="definicija">dobro premeša</span> po času $t_{mix}(\theta)$. Ta koncept je seveda odvisen od izbire konstante $\theta$, a ponavadi za $\theta$ vzamemo kar neko majhno konstanto, na primer $\theta = 10^{-2}$.

[^16]: Tako hitra konvergenca je posledica dejstva, da je konjugiranostni razred $\conclass$ v $G_p$ zelo velik, $\log |\conclass| \sim \log |G_p|$, in da imamo zelo dobre ocene za $r_{\pi}(\conclass)$.

[^17]: Angleško *expander family*. Ime izhaja iz alternativne karakterizacije teh družin v teoriji grafov.

[^18]: Glej pregledni članek [(Liebeck 2017)](https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf).

[^19]: Ni težko premisliti, da sta ta dva koncepta ekvivalentna. Čas mešanja v vsaki članici družine $G_i$ je $O(\log |G_i|)$, če in samo če je družina ekspanzivna.
