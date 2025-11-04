```{raw} html
<style>
  body { counter-reset: chapter 5 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Razširjeni zgledi – neskončni

V tem zaključnem poglavju si bomo pogledali nekaj zgledov iz teorije upodobitev neskončnih grup. Tukaj ni enotne teorije, s katero bi lahko obravnavali vsako grupo, obstajajo pa družine grup, znotraj katerih lahko razumemo upodobitve na enoten način. Ne bomo razvijali splošne teorije, temveč si bomo ogledali le konkretne, a reprezentativne predstavnike nekaterih izmed pomembnih družin neskončnih grup.

### Ozaljšane upodobitve

V svetu neskončih grup ponavadi ne obravnavamo čisto vseh abstraktnih upodobitev, ker na ta način dobimo preprosto *preveč* upodobitev, ki niti niso *smiselne*.

<div class="zgled">

Opazujmo grupo $\RR$. Vemo že, da je vsaka njena končno razsežna nerazcepna kompleksna upodobitev enorazsežna, torej oblike $\chi \colon \RR \to \CC^*$ za nek homomorfizem $\chi$. Premislimo, da je takih homomorfizmov *ogromno*. Grupa $\RR$ je kot abelova grupa izomorfna neskončni direktni vsoti kopij $\ZZ$. Za vsak nabor realnih števil $x_1, x_2, \dots, x_k$, ki so $\ZZ$-linearno neodvisna, lahko izberemo poljuben nabor kompleksnih števil $z_1, z_2, \dots, z_k$ in dobimo homomorfizem abelovih grup $\chi \colon \RR \to \CC^*$ z lastnostjo $\chi(x_i) = z_i$ za vsak $i$.

</div>

To težavo zaobidemo tako, da ne opazujemo poljubnih upodobitev, temveč jih ozaljšamo z dodatnimi restrikcijami v odvisnosti od grupe, ki jo opazujemo.

#### Zveznost

Grupa $\RR$ ni le abstraktna grupa, temveč je opremljena s topologijo. Abstraktneje je <span class="definicija">topološka grupa</span> množica, ki je hkrati grupa in topološki prostor, obe strukturi pa sta uglašeni s pogojem, da sta operaciji množenja in invertiranja zvezni.

<div class="zgled">

Grupe $\RR$, $\RR^3$, $\RR^*$, $\U_1(\CC) = S^1$, $\SU_2(\CC)$, $\SO_3(\RR)$, $\GL_3(\CC)$, $\SL_2(\RR)$, $\SL_2(\ZZ)$ so topološke grupe. Vsaka od njih je opremljena z naravno topologijo, ki jo podeduje iz ambientalnega evklidskega prostora. Grupa $\SL_2(\ZZ)$ sicer podeduje le *diskretno* topologijo.

</div>

Končno razsežna[^1] kompleksna upodobitev $\rho \colon G \to \GL_n(\CC)$ topološke grupe $G$ je <span class="definicija">zvezna</span>, kadar je zvezna kot preslikava, pri čemer prostor $\GL_n(\CC) \subseteq \CC^{n^2}$ opremimo z inducirano topologijo.

<div class="zgled">

Nore upodobitve grupe $\RR$, ki smo jih konstruirali v zadnjem zgledu, povečini niso zvezne. So pa za vsak parameter $\zeta \in \CC$ zvezne upodobitve oblike
```{math}
\chi_{\zeta} \colon \RR \to \CC^*, \quad
    x \mapsto e^{\zeta x}.
```

</div>

Kadar je dana topološka grupa $G$ opremljena z znano topologijo, ki izhaja iz evklidskega prostora, kot se zgodi na primer v grupah $\SO_3(\RR)$ ali $\SL_2(\CC)$, ima smisel govoriti o mnogih dodatnih lastnostih matričnih koeficientov upodobitev. Lahko na primer zahtevamo, da so ti koeficienti gladki, analitični ali preprosto polinomi. V teh primerih rečemo, da imamo gladko, analitično oziroma polinomsko upodobitev.

#### Unitarnost

Pri raziskovanju teorije upodobitev končnih grup nam je marsikje prav prišlo dejstvo, da smo vektorske prostore opremili s skalarnim produktom, ki je bil invarianten glede na upodobitev. Z drugimi besedami, opazovali smo <span class="definicija">unitarne</span> upodobitve, ki slikajo v grupo $\U(V) \leq \GL(V)$. Z metodo povprečenja smo dokazali, da je vsaka upodobitev končne grupe unitarizabilna in torej po ustrezni zamenjavi baze lahko predpostavimo, da je oblike $\rho \colon G \to U_n(\CC)$. Za neskončne grupe tega sklepa ne moremo napraviti in tudi zaključek v splošnem ne drži.

<div class="zgled">

Opazujmo grupo $\RR$ in njene upodobitve $\chi_{\zeta}$. Ta upodobitev je unitarna, če in samo če za nek skalarni produkt na $\CC$ velja
```{math}
\langle u, v \rangle = \langle e^{\zeta x} u, e^{\zeta x} v \rangle
```
za vsak $x \in \RR$ in vse $u,v \in \CC$. Ta pogoj je enakovreden $|e^{\zeta x}| = 1$, se pravi $\zeta \in \RR \cdot i$. V tem primeru upodobitev $\chi_{\zeta}$ nujno slika v enotsko krožnico $\U(\CC) = S^1 = \{ z \in \CC \mid |z| = 1 \}$.

</div>

Za neskončne topološke grupe najraje opazujemo zvezne unitarne upodobitve. O teh ponavadi lahko povemo največ, kot bomo videli v nadaljevanju.

## Kompaktne grupe

Večino rezultatov iz končnih grup lahko prenesemo v svet kompaktnih topoloških grup in njihovih zveznih unitarnih upodobitev.

### $\U_1(\CC)$

Najenostavnejši primer neskončne kompaktne grupe je unitarna grupa $\U_1(\CC) = S^1$ kompleksnih števil absolutne vrednosti $1$. To topološko grupo lahko alternativno vidimo kot $\RR/\ZZ$ s kvocientno topologijo iz grupe $\RR$.

#### Nerazcepne upodobitve

Poznamo že nekaj upodobitev grupe $\RR/\ZZ$, ki jih ponuja grupa $\RR$, in sicer za vsak parameter $k \in \ZZ$ dobimo upodobitev
```{math}
\chi_k \colon \RR/\ZZ \to \CC^*, \quad
    x \mapsto e^{2 \pi i k x}.
```
Velja pa tudi obratno, iz vsake upodobitve $\chi \colon \RR/\ZZ \to \U_1(\CC)$ z restrikcijo vzdolž $\RR \to \RR/\ZZ$ dobimo upodobitev $\RR$. Te upodobitve lahko popolnoma opišemo s pomočjo elementarne analize.

<div class="trditev">

Vsaka zvezna upodobitev $\RR \to \CC^*$ je oblike $\chi_{\zeta}$ za nek $\zeta \in \CC$.

</div>

<div class="dokaz">

Naj bo $\chi \colon \RR \to \CC^*$ zvezna. Če je $\chi$ celo *odvedljiva*, potem za vsak $x \in \RR$ velja
```{math}
\chi^\prime(x) 
    = \lim_{t \to 0} \frac{\chi(x + t) - \chi(x)}{t}
    = \chi(x) \chi^\prime(0).
```
Funkcija $\chi$ torej reši diferencialno enačbo $\chi^\prime = \zeta \chi$, kjer smo označili $\zeta = \chi^\prime(0)$. Od tod sledi, da je $\chi(x) = A \cdot e^{\zeta x}$ za neko konstanto $A$. Vstavimo $x = 0$ in sklenemo $A = 1$, torej je res $\chi = \chi_{\zeta}$.

Prepričajmo se, da je $\chi$ *vselej* odvedljiva, s čimer bo trditev dokazana. V ta namen jo najprej integrirajmo do odvedljive funkcije
```{math}
X \colon \RR \to \CC, \quad 
    x \mapsto \int_{0}^{x} \chi(t) dt.
```
Funkcija $X$ sicer ni nujno homomorfizem, velja pa
```{math}
X(x + y)
    = X(x) + \int_{x}^{x+y} \chi(t) dt
    = X(x) + \int_{0}^{y} \chi(t+x) dt
    = X(x) + \chi(x) X(y)
```
za vsaka $x,y \in \RR$. Ker je $X^\prime = \chi$, seveda obstaja $y_0 \in \RR$, za katerega je $X(y_0) \neq 0$. Od tod lahko izrazimo $\chi(x)$ kot
```{math}
\chi(x) = \frac{X(x+y_0) - X(x)}{X(y_0)}.
```
Ker je funkcija na desni odvedljiva, velja enako tudi za funkcijo na levi.

</div>

Iz trditve izpeljemo, da vsaka zvezna upodobitev $\RR/\ZZ \to \CC^*$ izhaja iz upodobitve $\chi_{\zeta}$ za nek $\zeta$. Pri tem mora biti $\ZZ \leq \ker \chi_{\zeta}$, od koder sledi $\zeta = 2 \pi i k$ za nek $k \in \ZZ$. Upodobitve $\chi_k$ torej izčrpajo vse končno razsežne zvezne kompleksne upodobitve grupe $\RR/\ZZ$. Te upodobitve so vse tudi unitarne, kar ni naključje, kot bomo pojasnili nekoliko kasneje.

#### Fourierova analiza

Klasična Fourierova analiza periodičnih funkcij se tesno prepleta s teorijo upodobitev grupe $\RR/\ZZ$. Kot vemo, lahko z upodobitvami $\chi_k$ za $k \in \ZZ$ aproksimiramo poljubno zvezno funkcijo na $\RR/\ZZ$. To naredimo na sledeč način. Prostor funkcij na grupi $\RR/\ZZ$ opremimo s skalarnim produktom
```{math}
\langle f, h \rangle = \int_{0}^{1} f(t) \overline{h(t)} dt.
```
Fourierovi koeficienti funkcije $f$ so
```{math}
\langle f, \chi_k \rangle = \int_0^1 f(t) e^{-2 \pi i k t} dt
```
za $k \in \ZZ$. Z njimi definiramo delne Fourierove vsote
```{math}
f_N = \sum_{k \in \ZZ \colon |k| \leq N} \langle f, \chi_k \rangle \chi_k
```
za $N \in \NN$. V splošnem delne vsote $f_N$ ne konvergirajo po točkah,[^2] je pa temu tako, če dodatno predpostavimo, da obravnavamo le kvadratno integrabilne funkcije $f$, se pravi
```{math}
\int_0^1 |f(t)|^2 dt < \infty.
```
Za te funkcije po osnovnem izreku Fourierove analize velja konvergenca
```{math}
\lim_{N \to \infty} || f - f_N || = 0,
```
torej lahko $f$ razvijemo v Fourierovo vrsto. Pri tem moramo biti nekoliko previdni, saj opisana konvergenca *ne* implicira, da vrsta $f_N$ v vseh točkah konvergira k $f$, temveč le *skoraj povsod*. Hkrati drži varianta Parsevalove formule
```{math}
||f||^2 = \sum_{k \in \ZZ} |\langle f, \chi_k \rangle|^2.
```
Upodobitve $\chi_k$ za $k \in \ZZ$ torej tvorijo ortonormiran sistem funkcij, ki je *gost* v prostoru vseh dovolj lepih funkcij na $\RR/\ZZ$.

<div class="zgled">

Opazujmo funkcijo $f \colon \RR/\ZZ \to \RR$, definirano kot
```{math}
f(x) = - 2 \log | 2 \sin(\pi x) |
```
z vrednostjo $f(0) = 0$ v singularni točki. Pišimo $z = e^{2 \pi i x}$. Potem je $\Re(2 \log (1 - z)) = 2 \log |1 - z| = \log |\sin(\pi x)|$. Uporabimo razvoj $- \log(1 - z) = \sum_{k \geq 1} z^k / k$,[^3] da dobimo
```{math}
f(x) = 
    2 \sum_{k \geq 1} \frac{\cos(2 \pi k x)}{k} 
    = \sum_{k \neq 1} \frac{1}{|k|} \chi_k(x)
```
za $0 < x < 1$. Fourierovi koeficienti funkcije $f$ so torej $\langle f, \chi_k \rangle = 1/|k|$ za $k \neq 0$ in $\langle f, \chi_0 \rangle = 0$. Vsota kvadratov teh koeficientov konvergira, zato je po [Riesz-Fischerjevem izreku](https://en.wikipedia.org/wiki/Riesz–Fischer_theorem) $f$ kvadratno integrabilna funkcija na $\RR/\ZZ$. Delne Fourierove vsote $f_N$ so v točki $x = 0$ enake
```{math}
f_N(0) = 2 \sum_{1 \leq k \leq N} \frac{1}{k},
```
kar divergira za $N \to \infty$.

</div>

Fourierovo analizo lahko torej vidimo kot analog dekompozicije regularne upodobitve v primeru končnih grup za neskončno grupo $\RR/\ZZ$.

### Poljubne kompaktne grupe

Izkaže se, da ima vse, kar smo videli za primer $\U_1(\CC)$, ustrezno posplošitev za poljubno kompaktno grupo $G$, na primer $\SU_2(\CC)$ ali $\SO_3(\RR)$. Za natančno obravnavo potrebujemo nekaj *teorije mere*, ki jo bomo prosto uporabili v tem podrazdelku.[^4]

V primeru grupe $\RR/\ZZ$ smo skalarni produkt na prostoru funkcij izrazili s pomočjo integrala. Izkaže se, da ima vsaka kompaktna grupa enolično verjetnostno mero $\mu$, ki zadošča pogoju invariantnosti $\mu(U) = \mu(g \cdot U) = \mu(U \cdot g)$ za vsako merljivo množico $U$ in element $g \in G$. To mero imenujemo <span class="definicija">Haarova mera</span>.[^5]

<div class="zgled">

Multiplikativna grupa $\U_1(\CC) = S^1$ je izomorfna aditivni grupi $\RR/\ZZ$ preko preslikave $\chi_1 \colon \RR/\ZZ \to S^1$, $x \mapsto e^{2 \pi i x}$. Naj bo $\lambda$ standardna Lebesgueova mera na $\RR$. To mero lahko preko kanonične projekcije $\RR \to \RR/\ZZ$ prenesemo na $\RR/\ZZ$, pri čemer definiramo mero na podmnožici $U \subseteq \RR/\ZZ$ kot $\lambda(\pi^{-1}(U) \cap [0,1))$. Za pripadajočo podmnožico $U \subseteq S^1$ potem definiramo njeno mero kot $\mu(U) = \lambda(\chi_1^{-1}(U))$. Ta mera je Haarova mera na $\U_1(\CC)$ in igra ključno vlogo v klasični Fourierovi analizi, kot smo se spomnili zgoraj.

</div>

<div class="zgled">

Nekoliko bolj zapleten opis ima Haarova mera na grupi $\SU_2(\CC)$. Elementi te grupe so matrike oblike
```{math}
\begin{pmatrix}
        a & b \\
        -\overline{b} & \overline{a}
    \end{pmatrix}, \quad |a|^2 + |b|^2 = 1.
```
Grupo $\SU_2(\CC)$ lahko torej identificiramo s sfero $S^3 \subseteq \RR^4$ preko vložitve $\iota(a,b) = (\Re(a), \Im(a), \Re(b), \Im(b))$. Mero na $\SU_2(\CC)$ potem definiramo preko Lebesgueove mere na $S^3$.

Oglejmo si, kako to deluje v koordinatah. Parametrizirajmo $a,b$ in s tem vložitev $\iota$ kot $a = e^{\frac{i}{2} (\phi + \psi)} \cos(\theta/2)$ in $b = e^{\frac{i}{2} (\phi - \psi)} \sin(\theta/2)$ za realna števila $\phi \in [0, 2\pi)$, $\theta \in [0, \pi]$, $\psi \in [0, 4\pi)$. Naj bodo $v_1, v_2, v_3$ tangentni vektorji na $S^3$, dobljeni z odvajanjem vložitve $\iota$ po parametrih $\phi, \psi, \theta$. Ti vektorji napenjajo paralelepiped z volumnom $\sqrt{\det(G)}$, kjer je $G$ Gramova matrika z elementi $G_{ij} = \langle v_i, v_j \rangle$. Izračunamo
```{math}
G = \begin{pmatrix}
    1/4 & 0 & \cos(\theta)/4 \\
    0 & 1/4 & 0 \\
    \cos(\theta)/4 & 0 & 1/4
\end{pmatrix}, \quad \det(G) = \frac{\sin^2(\theta)}{64}.
```
Diferencialen volumen na $S^3$ glede na izbrano parametrizacijo je torej $\frac{\sin(\theta)}{8} d\phi d\theta d\psi$. Ko to pointegriramo po celotni domeni parametrov, dobimo volumen sfere $2 \pi^2$. Haarova mera je verjetnostna, zato moramo diferencialen volumen še normalizirati s faktorjem $1/(2 \pi^2)$. Končno dobimo Haarovo mero na $\SU_2(\CC)$ z gostoto $\frac{\sin(\theta)}{16 \pi^2}$ v parametrih $\phi, \theta, \psi$.

</div>

S Haarovo mero lahko definiramo integral merljive funkcije. S pomočjo tega se nam odprejo vrata orodju povprečenja po grupi, ki ga lahko izkoristimo za različne namene.

<div class="trditev">

Vsaka zvezna končno razsežna kompleksna upodobitev kompaktne grupe je unitarizabilna.

</div>

<div class="dokaz">

Naj bo $\rho \colon G \to \GL(V)$ upodobitev. Izberemo poljuben skalarni produkt $\langle \cdot, \cdot \rangle$ na $V$ in ga povprečimo do
```{math}
\langle \cdot, \cdot \rangle_0 \colon V \times V \to \CC, \quad
    \langle v, w \rangle_0 = \int_{G} \langle \rho(g) \cdot v, \rho(g) \cdot w \rangle d \mu (g).
```
Ni težko preveriti, da je $\langle \cdot, \cdot \rangle_0$ skalarni produkt na $V$, glede na katerega je $\rho$ unitarna upodobitev.

</div>

Kot v primeru $\RR/\ZZ$ lahko vse upodobitve najdemo v ustreznem modelu regularne upodobitve. V splošnem opazujemo funkcije na kompaktni grupi $G$, pri čemer se omejimo na prostor kvadratno integrabilnih merljivih funkcij in še te opazujemo le do ekvivalence *skoraj povsod* natančno. Prostor ekvivalenčnih razredov takih funkcij je $L^2(G)$. Na tem prostoru deluje grupa $G$ kot regularna upodobitev,
```{math}
\rho(g) \cdot f = x \mapsto f(x g).
```
Ta prostor je seveda neskončno razsežen. Znameniti Peter-Weylov izrek razkrije dekompozicijo te upodobitve, ki je popolnoma analogna tisti iz sveta končnih grup.[^6]

<div class="izrek">

Naj bo $G$ kompaktna grupa s Haarovo mero $\mu$. Regularna upodobitev $G$ na $L^2(G)$ je izomorfna ortogonalni direktni vsoti Hilbertovih prostorov
```{math}
L^2(G) \cong \bigoplus_{\pi} \underbrace{\pi \oplus \pi \oplus \cdots \oplus \pi}_{\deg(\pi)},
```
ko $\pi$ preteče vse končno razsežne nerazcepne zvezne unitarne upodobitve grupe $G$.

</div>

Kot v končnih grupah se s pomočjo matričnih koeficientov prepričamo, da je vsaka nerazcepna zvezna unitarna upodobitev vsebovana v regularni. V posebnem je zato vsaka zvezna unitarna upodobitev kompaktne grupe nujno *končno razsežna*.

## Zvezne linearne grupe

V tem razdelku si bomo ogledali, kako lahko razumemo teorijo upodobitev linearnih topoloških grup, ki lokalno izgledajo kot $\RR^n$ ali $\CC^n$. To so na primer grupe $\GL_n(\CC)$, $\SL_2(\CC)$, $\SL_2(\RR)$, $\SO_3(\RR)$, $\SU_2(\CC)$. Zadnji dve grupi sta sicer kompaktni, tako da ju lahko razumemo tudi z orodji zadnjega razdelka. Tu se bomo zato osredotočili na nekompaktne zglede.

### $\SL_2(\CC)$

Grupa $\SL_2(\CC)$ je zaprta podmnožica kompleksnega prostora $\CC^4$, dana z enačbo $ad - bc = 1$. Ker je odvod determinantne preslikave v vsaki točki neničeln, je $\SL_2(\CC)$ podmnogoterost kompleksne razsežnosti $3$. Pri opazovanju upodobitev grupe $\SL_2(\CC)$ bomo seveda upoštevali to strukturo, saj sicer dobimo *preveč* updobitev.[^7] Smiselno bo opazovati upodobitve, pri katerih so matrični koeficienti zvezne ali celo gladke funkcije matrike, ki deluje. Glede na to, da je $\SL_2(\CC)$ kompleksna mnogoterost, lahko opazujemo tudi kompleksno analitične upodobitve. Na grupo $\SL_2(\CC)$ lahko gledamo tudi kot na algebraično grupo,[^8] zato ima smisel opazovati tudi le polinomske upodobitve. Kot bomo videli, so si nazadnje vse te različne oblike upodobitev grupe $\SL_2(\CC)$ med sabo zelo podobne.

#### Standardna upodobitev in njene potence

Grupa $\SL_2(\CC)$ naravno deluje na vektorskem prostoru $\CC^2$ z množenjem matrik z vektorji. Označimo bazna vektorja kot $X = e_1$ in $Y = e_2$. Na ta način dobimo <span class="definicija">standardno upodobitev</span>
```{math}
\rho_1 \colon {\textstyle \SL_2(\CC) \to \GL_2(\CC)}, \quad
    \begin{pmatrix}
        a & b \\ c & d 
    \end{pmatrix}
    \mapsto \left( (X,Y) \mapsto (X,Y) \cdot \begin{pmatrix}
        a & b \\ c & d 
    \end{pmatrix} \right).
```
To upodobitev lahko vidimo kot upodobitev na prostoru linearnih polinomov v $X$,$Y$. V tej luči jo lahko naravno razširimo na prostor homogenih polinomov $\CC[X,Y]_k$ stopnje $k \geq 1$.[^9] Baza tega prostora so monomi $e_i = X^i Y^{k-i}$ za $0 \leq i \leq k$, torej je $\CC[X,Y]_k$ razsežnosti $k+1$. Formalno za razširitev $\rho_1$ uporabimo simetrično potenco in dobimo
```{math}
{\textstyle \rho_k = \Sym^k(\rho_1) \colon \SL_2(\CC) \to \GL(\CC[X,Y]_k),} \quad
    g \mapsto \left( f(X,Y) \mapsto f((X,Y) \cdot g) \right).
```
Eksplicitno se bazni monom $e_i = X^i Y^{k-i}$ z upodobitvijo $\rho_k$ preslika v
```{math}
\rho_k \begin{pmatrix}
        a & b \\ c & d 
    \end{pmatrix}
    \cdot X^i Y^{k-i}
    = (aX + cY)^i (bX + dY)^{k-i},
```
kar brez težave razvijemo po monomih v $\CC[X,Y]_k$. Pri tem dobimo koeficiente, ki so polinomi v spremenljivkah $a,b,c,d$, zato je upodobitev $\rho_k$ polinomska.

<div class="trditev">

Polinomske upodobitve $\rho_k \colon \SL_2(\CC) \to \GL_{k+1}(\CC)$ so nerazcepne.

</div>

<div class="dokaz">

Kot v obravnavi upodobitev splošne linearne grupe nad končnim poljem si oglejmo torus[^10]
```{math}
T = \left\{ 
        \begin{pmatrix}
            \lambda & 0 \\ 0 & \lambda^{-1}
        \end{pmatrix}        
        \mid
        \lambda \in \CC^*
    \right\} \cong \CC^*.
```
Upodobitev $\rho_k$ zožimo na $T$. Velja
```{math}
\rho_k \begin{pmatrix}
        \lambda & 0 \\ 0 & \lambda^{-1}
    \end{pmatrix}
    \cdot e_i
    = \lambda^{2i - k} e_i.
```
Naj bo $\chi_i$ upodobitev $T \cong \CC^* \to \CC^*$, $\lambda \mapsto \lambda^i$. Imamo torej zelo preprosto dekompozicijo
```{math}
{\textstyle \Res^{\SL_2(\CC)}_T(\rho_k)}
    = 
    \chi_{-k} \oplus \chi_{-k+2} \oplus \cdots \oplus \chi_{k}.
```
S pomočjo tega bomo dokazali, da je $\rho_k$ nerazcepna upodobitev. Res, naj bo $0 \neq W \leq \CC[X,Y]_k$ poljuben $\SL_2(\CC)$-invarianten podprostor. Ker je $\Res^{\SL_2(\CC)}_T(\rho_k)$ polenostavna upodobitev, v kateri vsaka nerazcepna podupodobitev nastopa z večkratnostjo $1$, podprostor $W$ nujno sestoji iz nekaterih od teh podupodobitev. Za neko množico $I \subseteq \{ 0,1,\dots,k\}$ torej velja
```{math}
W = \bigoplus_{i \in I} \CC \cdot e_i.
```
Upoštevajmo zdaj, da je $W$ invarianten še glede na vse ostale elemente v $\SL_2(\CC)$. Velja
```{math}
\rho_k \begin{pmatrix}
        1 & 1 \\ 0 & 1
    \end{pmatrix}
    \cdot e_i
    = X^i (X+Y)^{k-i}
    = \sum_{j = i}^k \binom{k-i}{j-i} e_j.
```
Če je $e_{i_0} \in W$, je torej $e_i \in W$ za vsak $i \geq i_0$, saj je $W$ razpet z nekaterimi standardnimi baznimi vektorji. Podoben argument s spodnjetrikotno matriko pokaže, da je $e_i \in W$ za vsak $i \leq i_0$. Sklepamo torej $W = \CC[X,Y]_k$ in $\rho_k$ je res nerazcepna upodobitev.

</div>

Na ta način smo torej konstruirali neskončno mnogo nerazcepnih polinomskih upodobitev grupe $\SL_2(\CC)$ poljubne visoke stopnje. Zanimivo je, da te upodobitve *niso* unitarne. Lastne vrednosti unitarnih matrik so namreč nujno absolutne vrednosti $1$, čemur upodobitve $\rho_k$ ne zadoščajo. Kasneje bomo videli preprost argument, da niti njena podgrupa $\SL_2(\RR)$ nima netrivialnih končno razsežnih unitarnih upodobitev. Upodobitve teh grup so torej bistveno drugačne od upodobitev kompaktnih grup, kjer so *vse* končno razsežne nerazcepne upodobitve unitarne.

<div class="domacanaloga">

Grupa $\SU_2(\CC)$ je kompaktna podgrupa $\SL_2(\CC)$. Dokaži, da so zožitve upodobitev $\rho_k$ na $\SU_2(\CC)$ nerazcepne in unitarne. Izračunaj karakter vsake od teh upodobitev in dokaži, da te funkcije tvorijo gosto bazo prostora $L^2(\SU_2(\CC))$. To so torej vse zvezne nerazcepne unitarne upodobitve grupe $\SU_2(\CC)$.

</div>

#### Linearizacija upodobitve

Princip za dokazovanje, da smo z upodobitvami $\rho_k$ izčrpali vse dovolj lepe upodobitve grupe $\SL_2(\CC)$, temelji na *linearizaciji*. Vsako odvedljivo upodobitev $\rho \colon \SL_2(\CC) \to \GL_n(\CC)$ lahko namreč obravnavamo kot preslikavo med mnogoterostmi, zato z njenim <span class="definicija">odvodom</span> dobimo inducirano linearno preslikavo
```{math}
\textstyle D_I \rho \colon T_I \SL_2(\CC) \to T_I \GL_n(\CC)
```
med tangentnima prostoroma v identični matriki. Oglejmo si podrobneje, kako izgledata ta dva tangentna prostora in kaj točno je $D_I \rho$.[^11]

Opazujmo najprej grupo $\GL_n(\CC)$, ki je odprta podmnožica $\CC^{n^2}$. Njen tangentni prostor v $I$ zato lahko identificiramo z vektorskim prostorom $\CC^{n^2}$, ki ga predstavimo v matrični obliki kot
```{math}
\textstyle \glfrak_n(\CC) = \{ X \mid X \in \Mat_{n}(\CC) \}.
```
Ta opis je prikladen, ker omogoča jasen opis majhne okolice $I$ v $\GL_n(\CC)$. Za vsak tangentni vektor $X \in \glfrak_n(\CC)$ imamo preslikavo $\RR \to \glfrak_n(\CC)$, $t \mapsto tX$, ki jo lahko potisnemo v $\GL_n(\CC)$ z <span class="definicija">eksponentno preslikavo</span> in dobimo gladko pot
```{math}
\gamma \colon \RR \to {\textstyle \GL_n(\CC)}, \quad
    t \mapsto e^{tX} = \sum_{i = 0}^{\infty} t^i X^i / i!
```
v grupi $\GL_n(\CC)$. Res, velja formula $\det(\gamma(t)) = \det e^{tX} = e^{\tr (tX)}$,[^12] zato je $\gamma(t)$ obrnljiva matrika. Tangentni vektor poti $\gamma$ v točki $0$ izračunamo kot
```{math}
D_0 \gamma 
    = \lim_{t \to 0} \frac{e^{tX} - I}{t}
    = \lim_{t \to 0} \frac{I + tX + O(t^2) - I}{t}
    = X.
```
Pot $\gamma$ je torej gladka pot v $\GL_n(\CC)$ z začetno vrednostjo $\gamma(0) = I$ in tangentnim vektorjem $X$. Vsak tangentni vektor smo torej s pomočjo eksponentne preslikave uresničili kot tangentni vektor neke gladke poti skozi $I$. Vsaj lokalno pa je res tudi obratno: vsaka gladka pot v $\GL_n(\CC)$ v neki okolici $I$ izhaja iz gladke poti v $\glfrak_n(\CC)$, potisnjene v $\GL_n(\CC)$ z eksponentno preslikavo. To sledi neposredno iz naslednje lastnosti eksponentne preslikave.

<div class="trditev">

Eksponentna preslikava $e \colon \glfrak_n(\CC) \to \GL_n(\CC)$ je difeomorfizem v neki okolici $0$.

</div>

<div class="dokaz">

Na vsaki kompaktni podmnožici $\Omega \subseteq \glfrak_n(\CC)$ je vsak člen matrike $X$ absolutno omejen, recimo z $\alpha$, zato je tudi vsak člen matrike $X^k$ omejen z $n^{k-1} \alpha^k$. Po Weierstrassovem M-testu zato vrsta, ki definira eksponentno preslikavo, enakomerno konvergentna po kompaktih v $\glfrak_n(\CC)$. Delne vsote te vrste $\sum_{i = 0}^{k} X^i / i!$ so polinomske funkcije, zato so odvedljive. Iz povedanega sledi, da je eksponentna preslikava diferenciabilna v okolici $0$. Po izreku o inverzni preslikavi bo zdaj dovolj preveriti, da je linearna preslikava $D_0 e$ polnega ranga. Za poljuben $X \in \glfrak_n(\CC)$ naj bo $\lambda \colon \RR \to \glfrak_n(\CC)$, $t \mapsto tX$ in naj bo $\gamma = e \circ \lambda$. Po verižnem pravilu velja
```{math}
D_0 e \cdot X
    = D_0 e \cdot D_0 \lambda
    = D_0 \gamma
    = X.
```
Torej je $D_0 e$ kar identična preslikava.

</div>

Eksponentna preslikava ima torej lokalno inverz, ki ga označimo z $\log$. Za vsako gladko pot $\gamma \colon \RR \to \GL_n(\CC)$ z $\gamma(0) = I$ lahko torej najdemo $\epsilon > 0$, da je pot $\gamma |_{(-\epsilon, \epsilon)}$ oblike $e^{\lambda}$, kjer je $\lambda = \log \gamma \colon (-\epsilon, \epsilon) \to \glfrak_n(\CC)$ gladka pot v tangentnem prostoru.

S pomočjo eksponentne preslikave lahko dobro razumemo tudi tangentni prostor $T_I \SL_2(\CC)$ in njegovo lokalno povezavo z grupo $\SL_2(\CC)$. Izberimo poljuben tangentni vektor $X \in T_I \SL_2(\CC) \leq \glfrak_2(\CC)$. Obstaja torej gladka pot $\gamma \colon (-\epsilon, \epsilon) \to \SL_2(\CC)$ z odvodom $D_0 \gamma = X$. Po potrebi $\epsilon$ še zmanjšamo in s tem po zadnji trditvi dosežemo, da je $\gamma(t) = e^{\lambda(t)}$, kjer je $\lambda \colon (-\epsilon, \epsilon) \to T_I \SL_2(\CC)$ gladka pot. Pri tem velja
```{math}
X = D_0 \gamma
    = D_0 e \cdot D_0 \lambda
    = D_0 \lambda.
```
Ker $\gamma$ slika v $\SL_2(\CC)$, za vsak $t \in (- \epsilon, \epsilon)$ velja
```{math}
1 = \det (\gamma(t)) = e^{\tr(\lambda(t))},
```
zato je $\tr(\lambda(t)) = 0$ za vsak dovolj majhen $t$. To enakost odvedemo v točki $0$ in dobimo $\tr(X) = 0$. Vsak vektor v $T_I \SL_2(\CC)$ zato pripada vektorskemu prostoru
```{math}
\textstyle \slfrak_2(\CC) = \{ X \in \glfrak_2(\CC) \mid \tr(X) = 0 \}.
```
Res pa je tudi obratno. Vsak vektor $X$ s sledjo $0$ namreč določa pot $\gamma \colon \RR \to \SL_2(\CC)$, $t \mapsto e^{tX}$. Velja $\gamma(0) = I$ in $D_0 \gamma = X$, torej je $X \in T_I \SL_2(\CC)$.

<div class="posledica">

Velja $T_I \SL_2(\CC) = \slfrak_2(\CC)$. Ta vektorski prostor je $3$-razsežen z bazo
```{math}
e = \begin{pmatrix}
        0 & 1 \\ 0 & 0
    \end{pmatrix},
    \quad
    h = \begin{pmatrix}
        1 & 0 \\ 0 & -1
    \end{pmatrix},
    \quad
    f = \begin{pmatrix}
        0 & 0 \\ 1 & 0
    \end{pmatrix}.
```

</div>

Pod vsem povedanim lahko <span class="definicija">odvod upodobitve</span> $\rho \colon \SL_2(\CC) \to \GL_n(\CC)$ torej razumemo kot linearno preslikavo
```{math}
{\textstyle D_I \rho \colon \slfrak_2(\CC) \to \glfrak_n(\CC),} \quad
    X \mapsto D_0 \rho(e^{tX}),
```
ki tangentni vektor $X \in \slfrak_2(\CC)$ najprej pointegrira v pot $\gamma(t) = e^{tX}$ v $\SL_2(\CC)$ za vrednosti $t$ blizu $0$, to pot preslika z upodobitvijo $\rho$ v pot v $\GL_n(\CC)$ in izračuna odvod slednje poti, ki je tangentni vektor v $\glfrak_n(\CC)$.

<div class="zgled">

Linearizirajmo upodobitve $\rho_k \colon \SL_2(\CC) \to \GL(\CC[X,Y]_k)$. Najprej določimo slike generatorjev $e,h,f \in \slfrak_2(\CC)$ z eksponentno preslikavo. Za vsak $t \in \RR$ velja
```{math}
e^{te} = \begin{pmatrix}
        1 & t \\ 0 & 1
    \end{pmatrix}, \quad
    e^{th} = \begin{pmatrix}
        e^t & 0 \\ 0 & e^{-t}
    \end{pmatrix}, \quad
    e^{tf} = \begin{pmatrix}
        1 & 0 \\ t & 1
    \end{pmatrix}.
```
Naj bodo $E_k, H_k, F_k$ slike $e,h,f$ s preslikavo $D_I \rho_k$. Tangentni prostor $\glfrak_{k+1}(\CC)$ naravno deluje na prostoru $\CC[X,Y]_k$ z bazo $e_i = X^i Y^{k-i}$ za $0 \leq i \leq k$. Velja
```{math}
H_k \cdot e_i
    = D_0 \left( \rho_k(e^{th}) \cdot e_i \right)
    = D_0 \left( (e^t X)^i (e^{-t} Y)^{k-i} \right)
    = (2i - k) e_i,
```
na enak način izračunamo
```{math}
E_k \cdot e_i = (k-i) e_{i+1}, \quad
    F_k \cdot e_i = i e_{i-1}.
```
Element $H_k$ torej deluje diagonalno na $\CC[X,Y]_k$, pri čemer ima vektor $e_k = X^k$ največjo lastno vrednost, in sicer $k$. Ta vektor je v jedru preslikave $E_k$, z zaporednimi uporabami preslikave $F_k$ pa iz njega po vrsti dobimo vse ostale bazne vektorje $e_i$ za $0 \leq i \leq k$.

</div>

<figure>
<img src="img/img_sl2irrep.png" />
<figcaption>Prikaz delovanja elementov <span class="math inline"><em>E</em><sub><em>k</em></sub>, <em>H</em><sub><em>k</em></sub>, <em>F</em><sub><em>k</em></sub></span> v upodobitvi <span class="math inline"><em>ρ</em><sub><em>k</em></sub></span>.</figcaption>
</figure>

#### Liejeva algebra

Preslikava $D_I \rho$ ni čisto poljubna linearna preslikava med vektorskimi prostori, temveč v sebi skriva še nekaj dodatne informacije glede grup $\SL_2(\CC)$ in $\GL_n(\CC)$.

Grupa $\GL_n(\CC)$ deluje s konjugiranjem na svojem tangentnem prostoru,
```{math}
\textstyle \Ad \colon \GL_n(\CC) \to \End(\glfrak_n(\CC)), \quad
    A \mapsto \left( X \mapsto A X A^{-1} \right).
```
To delovanje imamo tudi z grupo $\SL_2(\CC)$ in njenim tangentnim prostorom, saj za vsak $X \in \slfrak_2(\CC)$ velja $\tr(AXA^{-1}) = \tr(X) = 0$.

Ni se težko prepičati, da je za vsak $A \in \SL_2(\CC)$ preslikava $D_I \rho$ *spletična* glede na to delovanje. Za vsak $Y \in \slfrak_2(\CC)$ velja namreč
```{math}
D_I \rho \cdot \Ad(A) \cdot Y
    = D_0 \left( \rho(e^{t A Y A^{-1}}) \right)
    = \Ad(\rho(A)) \cdot D_I \rho \cdot Y.
```
V posebnem za vsak tangentni vektor $X \in \slfrak_2(\CC)$ velja ta formula za $A = e^{tX}$. Izračunajmo odvod leve in desne strani v točki $t = 0$. Z uporabo verižnega pravila leva stran postane
```{math}
\textstyle D_I \rho \cdot D_0 \left( e^{tX} Y e^{-tX} \right)
    = D_I \rho \cdot (XY - YX),
```
desna stran pa postane
```{math}
\textstyle D_0 \left( \rho(e^{tX}) (D_I \rho \cdot Y) \rho(e^{-tX}) \right)
    = (D_I \rho \cdot X) (D_I \rho \cdot Y) -  (D_I \rho \cdot Y) (D_I \rho \cdot X).
```
Označimo $[X,Y] = XY - YX$. Velja torej
```{math}
D_I \rho \cdot [X,Y] = [D_I \rho \cdot X, D_I \rho \cdot Y],
```
kar pomeni, da preslikava $D_I \rho$ *spoštuje* operaciji $[\cdot, \cdot]$ na $\slfrak_2(\CC)$ in $\glfrak_n(\CC)$.

<div class="zgled">

V vektorskem prostoru $\slfrak_2(\CC)$ veljajo računi
```{math}
[h,e] = 2e, \quad
    [h,f] = -2f, \quad
    [e,f] = h.
```
Iz vrednosti $E_k$ in $F_k$ lahko zato izračunamo vrednost
```{math}
H_k \cdot e_i = D_I \rho_k (h) \cdot e_i = [E_k, F_k] \cdot e_i
    = i (k-(i-1)) e_i - (k-i) (i+1) e_i
    = (-k + 2i) e_i
```
za $0 \leq i \leq k$, kar se ujema z izračunom iz prejšnjega zgleda.

</div>

Na oba tangentna prostora zato gledamo kot na vektorska prostora, ozaljšana z binarno operacijo $[\cdot, \cdot]$. Ta operacija je bilinearna in kratek račun pokaže, da zadošča enakostima
```{math}
[X,Y] = -[Y,X], \quad [[X,Y], Z] + [[Y,Z], X] + [[Z,X], Y] = 0
```
za vse tangentne vektorje $X,Y,Z$. Abstraktnim vektorskim prostorom s tako binarno operacijo pravimo <span class="definicija">Liejeve algebre</span>. Te algebre tvorijo kategorijo: morfizmi med dvema algebrama so preslikave, ki spoštujejo vso strukturo, in jim zato upravičeno pravimo <span class="definicija">Liejevi homomorfizmi</span>.[^13] Kadar Liejev homomorfizem slika iz dane Liejeve algebre $L$ v $\glfrak_n(\CC)$, po analogiji z grupami rečemo, da imamo <span class="definicija">Liejevo upodobitev</span>. Te upodobitve lahko primerjamo med sabo s spletičnami in zato govorimo o izomorfnostnih razredih Liejevih upodobitev.[^14] Prav tako na smiseln način posplošimo pojem nerazcepne upodobitve.[^15]

Tangentna prostora $\slfrak_2(\CC)$ in $\glfrak_2(\CC)$ sta torej Liejevi algebri in odvod upodobitve $D_I \rho$ je Liejev homomorfizem, na katerega lahko gledamo kot na Liejevo upodobitev Liejeve algebre $\slfrak_2(\CC)$. Vsaka upodobitev grupe $\SL_2(\CC)$ nam torej da Liejevo upodobitev njene Liejeve algebre. Kadar ima upodobitev grupe kakšen netrivialen invarianten podprostor, je ta invarianten tudi za delovanje Liejeve algebre. Razcepne upodobitve grupe dajo torej razcepne upodobitve Liejeve algebre. Z drugimi besedami, nerazcepne upodobitve Liejeve algebre, ki izhajajo iz upodobitve grupe, lahko izhajajo le iz nerazcepnih upodobitev grupe. Zaradi tega je še posebej pomembno, da opišemo vse nerazcepne upodobitve Liejeve algebre.

<div class="zgled">

Liejeve upodobitve $D_I \rho_k$ so nerazcepne. Argument za to je podoben tistemu iz grup, a je še lažji. Res, če je $W \leq \CC[X,Y]_k$ netrivialen invarianten $\slfrak_2(\CC)$-podprostor, potem vsebuje vektor $0 \neq w = \sum_{i = 0}^k a_i e_i$. Naj bo $i_0$ največji indeks, za katerega je $a_{i_0} \neq 0$. Potem je $F_k^{i_0} \cdot w = a_{i_0} i_0! e_0 \in W$. Torej je $e_0 \in W$. Po zaporednih uporabah $E_k$ sklenemo $e_i \in W$ za vsak $0 \leq i \leq k$. Torej je res $W = \CC[X,Y]_k$.

</div>

<div class="trditev">

Vsaka nerazcepna Liejeva upodobitev Liejeve algebre $\slfrak_2(\CC)$ je izomorfna $D_I \rho_k$ za nek $k \geq 0$.

</div>

<div class="dokaz">

Naj bo $\phi \colon \slfrak_2(\CC) \to \glfrak_m(\CC) = \End(V)$ nerazcepna Liejeva upodobitev, kjer je $V = \CC^m$. Naj bodo $E,H,F$ slike $e,h,f$ s preslikavo $\phi$.

Naj bo $\lambda$ lastna vrednost $H$ in $v$ pripadajoči lastni vektor. Velja
```{math}
HEv = [H,E]v + EHv = 2 E v + \lambda E v = (\lambda + 2) Ev,
```
zato je $E \cdot \Eigenspace_{\lambda}(H) \subseteq \Eigenspace_{\lambda + 2}(H)$. Podobno velja $F \cdot \Eigenspace_{\lambda}(H) \subseteq \Eigenspace_{\lambda - 2}(H)$.

Izberimo lastno vrednost $\lambda$ preslikave $H$ z največjo možno realno komponento. Iz maksimalnosti $\lambda$ sledi $Ev \in \Eigenspace_{\lambda + 2}(H) = 0$. Naj bo $v_i = F^i v$ za $i \geq 0$.[^16] Velja $v_i \in \Eigenspace_{\lambda - 2i}(H)$. Za nek $n \geq 0$ velja torej $v_n \neq 0$ in $v_{n+1} = 0$. Vektorji $v_0, v_1, \dots, v_n$ so v različnih lastnih podprostorih $H$, zato so linearno neodvisni. Naj bo $W \leq V$ podprostor, ki ga generirajo.

Naj bo $w_i = E v_i$ za $i \geq 0$.[^17] Velja $w_0 = E v_0 = Ev = 0$, za $i \geq 1$ pa izračunamo
```{math}
w_i 
    = E F v_{i-1}
    = [E,F] v_{i-1} + FE v_{i-1}
    = H v_{i-1} + F w_{i-1}
    = (\lambda - 2i + 2) v_{i-1} + F w_{i-1}.
```
Velja torej $w_1 = \lambda v_0$. Od tod dobimo
```{math}
w_2 = (\lambda - 2) v_1 + F w_1
    = (\lambda - 2) v_1 + \lambda v_1
    = (2 \lambda - 2) v_1,
```
za tem
```{math}
w_3 = (\lambda - 4) v_2 + F w_2
    = (\lambda - 4) v_2 + (2\lambda - 2) v_2
    = (3 \lambda - 6) v_2
```
in induktivno
```{math}
w_i = i (\lambda - i + 1) v_{i-1}
```
za vsak $i \geq 1$. Prostor $W$ je torej invarianten za delovanje $\slfrak_2(\CC)$, zato po nerazcepnosti velja $V = W$.

Lastna vrednost $\lambda$ ni čisto poljubna. Velja namreč $\tr(H) = \tr([E,F]) = 0$, zato je vsota vseh lastnih vrednosti $H$ enaka $0$. Ta vsota je ravno
```{math}
\sum_{i = 0}^n (\lambda - 2i) = (n+1) \lambda - 2 (n+1)n/2
    = (n+1)(\lambda - n),
```
zato je $\lambda = n$. Od tod dobimo Liejevo spletično
```{math}
\alpha \colon V \to \CC[X,Y]_n, \quad
    v_i \mapsto \frac{n!}{(n-i)!} e_{n-i},
```
ki je izomorfizem Liejevih upodobitev $\phi$ in $D_I \rho_n$.

</div>

#### Integracija upodobitve

Vsaka upodobitev grupe $\SL_2(\CC)$ se odvede v Liejevo upodobitev Liejeve algebre $\slfrak_2(\CC)$. Neverjetno je, da velja tudi obratno: vsaka Liejeva upodobitev se pointegrira do upodobitve grupe.

<div class="trditev">

Naj bo $\phi \colon \slfrak_2(\CC) \to \glfrak_n(\CC)$ Liejeva upodobitev. Tedaj obstaja analitična upodobitev $\rho \colon \SL_2(\CC) \to \GL_n(\CC)$, za katero velja $D_I \rho = \phi$.

</div>

Dokaz te trditve sloni na uporabi eksponentne preslikave in njenega inverza $\log$. Naj bo $U \subseteq \SL_2(\CC)$ dovolj majhna okolica $I$, da je na njej $\log$ difeomorfizem v neko okolico enote $\slfrak_2(\CC)$. Po potrebi $U$ še zmanjšamo, da je $U^{-1} = U$ in da je $\log |_{U \cdot U}$ še vedno difeomorfizem. Vsaki matriki $A \in U$ lahko lahko priredimo $\log A$, ki jo s $\phi$ preslikamo v $\glfrak_n(\CC)$ in nazadnje dvignemo nazaj do grupe z eksponentno preslikavo. Na ta način dobimo gladko funkcijo
```{math}
\textstyle \rho \colon U \subseteq \SL_2(\CC) \to \GL_n(\CC), \quad
    A \mapsto e^{\phi(\log A)}.
```
Odvod te funkcije v $I$ je na tangentnem vektorju $X \in \slfrak_2(\CC)$ enak
```{math}
\textstyle D_I \rho \cdot X
    = D_0 \rho(e^{tX})
    = D_0 e^{\phi(\log e^{tX})}
    = D_0 e^{\phi(tX)}
    = D_0 e^{t \phi(X)}
    = \phi(X),
```
torej je $D_I \rho = \phi$ in smo $\phi$ pointegrirali na neko dovolj majhno okolico $I$.

Prepričajmo se, da je $\rho$ blizu tega, da bi bila homomorfizem. Naj bosta $A,B \in U$ poljubni matriki. Velja
```{math}
\rho(A) \rho(B) = e^{\phi(\log A)} e^{\phi(\log B)}, \quad
    \rho(AB) = e^{\phi(\log(AB))}.
```
Če bi logaritem pretvoril produkt v vsoto in eksponentna funkcija vsoto v produkt, potem bi iz linearnosti $\phi$ takoj sledilo, da sta oba izraza enaka. V splošnem žal matrični logaritem in eksponentna funkcija nimata te lastnosti. Za vsaka $X,Y \in \glfrak_n(\CC)$ lahko [z nekaj truda](https://www.math.ru.nl/~mueger/PDF/BCHD.pdf) z uporabo razvoja v Taylorjevo vrsto izračunamo vrednost
```{math}
\log(e^X e^Y) = X + Y + \frac{1}{2} [X,Y] - \frac{1}{12}[[X,Y],X] + \frac{1}{12} [[X,Y], Y] + \cdots,
```
ki ji pravimo <span class="definicija">Baker-Campbell-Hausdorffova formula</span>. Res torej v splošnem ne velja $\log(e^X e^Y) = X+Y$, tolažilna lastnost razvoja pa je, da so vsi členi izrazljivi z Liejevim produktom $[\cdot,\cdot]$ v $\glfrak_n(\CC)$. To pomeni, da za $A = e^X$, $B = e^Y$ velja
```{math}
\begin{aligned}
    \phi(\log(AB)) 
    &= \phi \left( X + Y + \frac{1}{2}[X,Y] + \cdots \right) \\
    &= \phi(X) + \phi(Y) + \frac{1}{2}[\phi(X), \phi(Y)] + \cdots \\
    &= \log(e^{\phi(\log A)} e^{\phi(\log B)}),
\end{aligned}
```
kjer smo v srednji enakosti upoštevali, da je $\phi$ Liejev homomorfizem. Od tod sklepamo, da res velja $\rho(A)\rho(B) = \rho(AB)$ za vsaka $A,B \in U$. Preslikava $\rho$ je torej vsaj lokalno homomorfizem.

Pogovorimo se še o tem, kako lahko razširimo $\rho$ na celo grupo $\SL_2(\CC)$. Prepričajmo se najprej, da množica $U$ generira grupo $\SL_2(\CC)$. Upodobitev bo torej enolično določena s svojimi vrednostmi na $U$. Izberimo poljuben $A \in \SL_2(\CC)$. Ker je $\SL_2(\CC)$ povezan topološki prostor, najdemo gladko pot $\gamma \colon [0,1] \to \SL_2(\CC)$ z $\gamma(0) = I$, $\gamma(1) = A$. Ta pot je na kompaktne intervalu enakomerno zvezna, zato obstajajo indeksi $0 = t_0 < t_1 < \cdots < t_m = 1$, tako da za vsaka $t_i \leq s < t \leq t_{i+1}$ velja $\gamma(t) \gamma(s)^{-1} \in U$. S tem lahko zapišemo
```{math}
A = \gamma(t_m)
    = \prod_{i = m}^1 \left( \gamma(t_i) \gamma(t_{i-1})^{-1} \right).
```
Ker je $\gamma(t_i) \gamma(t_{i-1})^{-1} \in U$, kjer že imamo definiran $\rho$, lahko definicijo razširimo na $A$ s predpisom
```{math}
\rho(A) = \prod_{i = m}^{1} \rho \left( \gamma(t_i) \gamma(t_{i-1})^{-1} \right).
```
Seveda moramo preveriti, da je ta definicija neodvisna od izbire delilnih točk $t_0, t_1, \dots, t_m$ in od izbire poti $\gamma$.

Prepričajmo se najprej, da z isto potjo $\gamma$ drugačna izbira delilnih točk privede do enakega rezultata, če je le zadoščeno pogoju $\gamma(t) \gamma(s)^{-1} \in U$ za vsaka $t_i \leq s < t \leq t_{i+1}$. V ta namen bo dovolj premisliti, da se definicija $\rho(A)$ ne spremeni, če fineje izberemo delilne točke, se pravi če dodamo še nekaj dodatnih točk.[^18] Za to pa bo dovolj preveriti, da se definicija $\rho(A)$ ne spremeni, če dodamo eno samo dodatno delilno točko, na primer med $t_i$ in $t_{i-1}$ vrinemo nek $s$. V tem primeru se v definiciji $\rho(A)$ spremeni le faktor $\rho(\gamma(t_i) \gamma(t_{i-1})^{-1})$, in sicer ga zamenjamo s produktom
```{math}
\rho(\gamma(t_i) \gamma(s)^{-1}) 
    \rho(\gamma(s) \gamma(t_{i-1})^{-1}).
```
Ker je $\rho$ homomorfizem na $U$, je zadnji člen enak $\rho(\gamma(t_i) \gamma(t_{i-1})^{-1})$, torej se vrednost $\rho(A)$ res ohrani pri dodajanju ene delilne točke. Definicija $\rho(A)$ je zato neodvisna od izbire delilnih točk.

Za neodvisnost od izbire poti potrebujemo nekaj *algebraične topologije*.

<div class="domacanaloga">

Dokaži najprej, da je $\SL_2(\CC)$ *enostavno povezan* topološki prostor. To lahko narediš tako, da Gram-Schmidtovo ortogonalizacijo izvedeš postopoma in na ta način *deformacijsko retraktiraš* $\SL_2(\CC)$ na $\SU_2(\CC)$. Slednja grupa je homeomorfna sferi $S^3$, ki je enostavno povezana.

Za neodvisnost definicije $\rho$ od izbire poti opazujmo dve poti v $\SL_2(\CC)$, imenujmo ju $\gamma_1$ in $\gamma_2$, ki povezujeta $I$ z $A$. Ker je $\SL_2(\CC)$ enostavno povezan topološki prostor, obstaja *homotopija* $H \colon [0,1] \times [0,1] \to \SL_2(\CC)$ z lastnostmi $H(0,t) = \gamma_1(t)$, $H(1,t) = \gamma_2(t)$, $H(s, 0) = 1$, $H(s,1) = A$. Po enakomerni zveznosti obstaja $N > 0$, da za vse $| s - s' | < 2/N$ in $| t - t'| < 2/N$ velja $H(s,t)H(s',t')^{-1} \in U$. Pokaži, da lahko s pomočjo homotopije $H$ pot $H(0,t) = \gamma_1(t)$ z zaporedjem majhnih perturbacij, ki ne vplivajo na vrednost $\rho(A)$, spremeniš v pot $H(1/N, t)$. Za tem slednjo pot z enakim argumentom spremeniš v pot $H(2/N, t)$ in tako naprej do poti $H(1,t) = \gamma_2(t)$. Vrednost $\rho(A)$ je torej res neodvisna od izbire poti $\gamma$.

</div>

S tem je dokaz trditve o integriranju Liejevih upodobitev $\slfrak_2(\CC)$ zaključen.

#### Nerazcepne upodobitve $\SL_2(\CC)$

Vzpostavili smo bijekcijo med analitičnimi upodobitvami grupe $\SL_2(\CC)$ in Liejevimi upodobitvami njene Liejeve algebre, ki ohranja nerazcepnost. Ker že poznamo nerazcepne upodobitve $\slfrak_2(\CC)$, dobimo vse nerazcepne analitične upodobitve grupe.

<div class="posledica">

Vsaka analitična nerazcepna končno razsežna kompleksna upodobitev grupe $\SL_2(\CC)$ je izomorfna $\rho_k$ za nek $k \geq 0$.

</div>

Na grupo $\SL_2(\CC)$ bi lahko gledali kot na *realno* grupo.[^19] V tem primeru bi njene *gladke* upodobitve dobili iz Liejevih upodobitev njene Liejeve algebre $\slfrak_2(\CC)$, na katero bi gledali kot na *realno* Liejevo algebro.[^20] Teh upodobitev je nekoliko več. Vsako od upodobitev $\rho_k$ lahko namreč še konjugiramo. Izkaže se, ni presenetljivo in ni težko, da vse nerazcepne realne Liejeve upodobitve dobimo kot tenzorske produkte teh.

<div class="posledica">

Vsaka gladka nerazcepna končno razsežna kompleksna upodobitev grupe $\SL_2(\CC)$ je izomorfna $\rho_k \otimes \overline{\rho_{\ell}}$ za neka $k, \ell \geq 0$.

</div>

Večino od povedanega v tem razdelku je razširljivo na poljubne topološke grupe, ki imajo strukturo realne ali kompleksne mnogoterosti, pri čemer sta množenje in invertiranje zvezni, gladki ali analitični operaciji. Takim grupam pravimo <span class="definicija">Liejeve grupe</span>.[^21] Eksaktno korespondenco med upodobitvami Liejeve grupe in njene prirejene Liejeve algebre izgubimo, če grupa ni enostavno povezana.

<div class="zgled">

Spomnimo se grupe $\U_1(\CC) \cong \RR/\ZZ$. Njena Liejeva algebra je $\RR$ s trivialnim Liejevim produktom in njene enorazsežne Liejeve upodobitve so linearne preslikave $\RR \to \CC$, torej so oblike $X \mapsto \zeta X$ za nek $\zeta \in \CC$. To upodobitev integriramo do lokalnega homomorfizma $x \mapsto e^{\zeta x}$, ki ga obravnavamo na majhni okolici enote v $\RR/\ZZ$. Ta preslikava se v splošnem *ne* razširi do homomorfizma na celotni grupi $\RR/\ZZ$. Se pa razširi do homomorfizma na *univerzalnem krovu* grupe $\RR/\ZZ$, ki je ravno $\RR$.

</div>

<div class="zgled">

Opazujmo grupo $\SU_2(\CC)$. Videli smo že, da je ta grupa homeomorfna sferi $S^3$. Grupa $\SU_2(\CC)$ je torej enostavno povezana realna Liejeva grupa. Podobno kot za grupo $\SL_2(\CC)$ se lahko prepričamo, da je Liejeva algebra $\sufrak_2(\CC)$ Liejeve grupe $\SU_2(\CC)$ enaka
```{math}
{\textstyle \sufrak_2(\CC)} = \left\{ \begin{pmatrix} i b & -c + i d \\ c + i d & - i b \\  \end{pmatrix} \mid b,c,d \in \RR \right\}.
```
Kot vektorski prostor je to $3$-razsežen realni vektorski prostor z bazo
```{math}
\begin{pmatrix}
        i & 0 \\ 0 & -i
    \end{pmatrix}, \quad
    \begin{pmatrix}
        0 & -1 \\
        1 & 0
    \end{pmatrix}, \quad
    \begin{pmatrix}
        0 & i \\ i & 0
    \end{pmatrix}.
```
Grupa $\SU_2(\CC)$ deluje s konjugiranjem na $\sufrak_2(\CC)$. Na ta način dobimo upodobitev
```{math}
\textstyle \Ad \colon \SU_2(\CC) \to \GL(\sufrak_2(\CC)) \cong \GL_3(\RR).
```

<div class="domacanaloga">

Prepričaj se, da je $\ker \Ad = \{ I, -I \}$ in da je $\image \Ad \cong \SO_3(\RR)$. Upodobitve grupe $\SO_3(\RR)$[^22] so torej ravno upodobitve enostavno povezane grupe $\SU_2(\CC)$, ki imajo v jedru $-I$.

</div>

</div>

### $\SL_2(\RR)$

Grupa $\SL_2(\RR)$ se pojavlja vsepočez matematike, predvsem prek svojih delovanj na različnih prostorih. Njene različne plasti odstira knjiga [(Lang 1985)](https://link.springer.com/book/10.1007/978-1-4612-5142-2). Zelo na kratko si bomo ogledali njeno bogato teorijo upodobitev.

#### Gladke upodobitve

Upodobitve $\rho_k$ grupe $\SL_2(\CC)$ lahko zožimo na podgrupo realnih matrik $\SL_2(\RR)$. Na ta način z analognim razmislekom kot v prejšnjem razdelku dobimo vse dovolj lepe upodobitve.

<div class="posledica">

Vsaka gladka nerazcepna končno razsežna kompleksna upodobitev grupe $\SL_2(\RR)$ je izomorfna $\rho_k$ za nek $k \geq 0$.

</div>

V kontekstu realnih Liejevih grup se sicer izkaže, da je vsaka zvezna končno razsežna upodobitev avtomatično gladka.[^23] To seveda ne velja za kompleksne Liejeve grupe, kjer lahko vsako analitično upodobitev konjugiramo in dobimo upodobitev, ki je sicer gladka, a ne nujno analitična. Upodobitve $\rho_k$ torej podajajo vse zvezne končno razsežne upodobitve grupe $\SL_2(\RR)$.

#### Unitarne upodobitve

Nobena od upodobitev $\rho_k$ ni unitarna. Če želimo konstruirati unitarne upodobitve, moramo poseči po neskončno razsežnih vektorskih prostorih. Te upodobitve lahko konstruiramo s pomočjo delovanj grupe $\SL_2(\RR)$. Ogledali si bomo en primer take konstrukcije.

Grupa $\SL_2(\RR)$ deluje na <span class="definicija">hiperbolični ravnini</span>
```{math}
\HH = \{  z \in \CC \mid \imaginary(z) > 0 \}
```
s predpisom
```{math}
\begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix}
    \cdot z
    =
    \frac{az + b}{cz + d}.
```
To delovanje je tranzitivno. Ni se težko prepričati, da stabilizator točke $i \in \HH$ sestoji iz kompaktne množice matrik
```{math}
{\textstyle \SO_2(\RR)} = \left\{ \begin{pmatrix} a & b \\ -b & a \end{pmatrix} \mid a^2 + b^2 = 1 \right\}
    \cong \U_1(\CC) = S^1.
```
Delovanje $\SL_2(\RR)$ na $\HH$ je torej ekvivalentno delovanju $\SL_2(\RR)$ na množici svojih desnih odsekov po kompaktni podgrupi $\SO_2(\RR)$. To permutacijsko delovanje na prostoru $\CC[\SL_2(\RR)/\SO_2(\RR)]$ lahko pretvorimo v upodobitev $\rho_k$ za vsak $k \geq 2$ z delovanjem na prostorih holomorfnih integrabilnih funkcij
```{math}
D_k = \left\{ f \colon \HH \to \CC \mid \text{$f$ holomorfna}, \ \int_{\HH} |f(z)|^2 y^k \frac{dx dy}{y^2} < \infty \right\},
```
in sicer definiramo
```{math}
\rho_k \colon {\textstyle \SL_2(\RR)} \to \GL(D_k), \quad
    \rho_k \begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix}
    \cdot f (z)
    = (-cz + a)^{-k} \cdot f\left( \begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix}^{-1} \cdot z \right).
```
Izkaže se, da je $\rho_k$ nerazcepna unitarna upodobitev grupe $\SL_2(\RR)$ na neskončno razsežnem Hilbertovem prostoru $D_k$ in da so te upodobitve med sabo neizomorfne. Na ta način dobimo celo vrsto nerazcepnih unitarnih upodobitev grupe $\SL_2(\RR)$, ki jim pravimo <span class="definicija">upodobitve diskretne vrste</span>.

Z opazovanjem drugih zanimivih podgrup v $\SL_2(\RR)$ najdemo še kakšne druge unitarne upodobitve. Še posebej zanimiva je diskretna podgrupa $\SL_2(\ZZ)$. Z njo dobimo kvocientno množico $Y = \SL_2(\ZZ) \backslash \SL_2(\RR)$. Na grupo $\SL_2(\RR)$ lahko s pomočjo projekcije $\SL_2(\RR) \to \SL_2(\RR)/\SO_2(\RR) = \HH$ prenesemo mero, ki jo nato potisnemo na $Y$, tako da lahko opazujemo prostor funkcij $L^2(Y)$, na katerem deluje grupa $\SL_2(\RR)$. V tem prostoru lahko najdemo mnogo nerazcepnih unitarnih podupodobitev. Še posebej zanimive so upodobitve, ki so konsturirane s pomočjo indukcije unitarnih upodobitev Borelove podgrupe zgornjetrikotnih matrik. Te imenujemo <span class="definicija">upodobitve glavne vrste</span> in jih lahko vidimo kot posplošitev upodobitev glavne vrste iz teorije upodobitev grupe $\GL_2(\FF_p)$.

Poleg teh dveh družin upodobitev ima grupa $\SL_2(\RR)$ še eno nekoliko bolj nenavadno družino unitarnih nerazcepnih upodobitev, ki jih dobimo z indukcijo določenih *neunitarnih* upodobitev Borelove podgrupe. Te upodobitve tvorijo družino <span class="definicija">upodobitev komplementarne vrste</span>.

Izkaže se, da vse netrivialne nerazcepne unitarne upodobitve grupe $\SL_2(\RR)$ lahko dobimo iz ene od opisanih družin upodobitev.

Razumevanje neskončno razsežnih nerazcepnih unitarnih upodobitev poljubnih Liejevih grup je eden od pomembnih nedoseženih ciljev teorije upodobitev. Nekaj znanih rezultatov skupaj z vizijo o tem, kako naprej, je predstavljenih v zelo dostopnem članku [(Vogan 2007)](https://math.mit.edu/~dav/articleHIST.pdf).

## Diskretne linearne grupe

Nazadnje si bomo pogledali še nekaj zgledov upodobitev diskretnih neskončnih grup, in sicer $\SL_m(\ZZ)$. V zadnjem zgledu smo videli, da te igrajo vlogo pri opisovanju unitarnih upodobitev Liejevih grup. Te grupe niso ozaljšane z uporabno topologijo, zato bomo opazovali kar običajne abstraktne končno razsežne kompleksne upodobitve. Kot bomo videli, se te grupe obnašajo bistveno različno za $m = 2$ oziroma za $m \geq 3$.

### $\SL_2(\ZZ)$

#### Osnovne poteze

Grupa $\SL_2(\ZZ)$ je diskretna podgrupa Liejeve grupe $\SL_2(\CC)$. Ta grupa je opremljena z naravnim <span class="definicija">kongruenčnim homomorfizmom</span>
```{math}
\textstyle \pi_N \colon \SL_2(\ZZ) \to \SL_2(\ZZ/N\ZZ)
```
za vsako naravno število $N$, ki vnose matrike reducira po modulu $N$.

<div class="domacanaloga">

Preveri, da je $\pi_N$ surjektivna za vsak $N \in \NN$.

</div>

V posebnem za vsako praštevilo $p$ dobimo homomorfizem v grupo $\SL_2(\FF_p)$, ki jo že dobro poznamo. Z analognim argumentom kot v primeru tega končnega kvocienta se prepričamo, da matriki
```{math}
S_+ = \begin{pmatrix}
        1 & 1 \\ 0 & 1
    \end{pmatrix},
    \quad
    S_- = \begin{pmatrix}
        1 & 0 \\ 1 & 1
    \end{pmatrix}
```
generirata grupo $\SL_2(\ZZ)$. V tej neskončni grupi se sicer izkaže, da nam bolj prav prideta matriki
```{math}
A = S_+^{-1} S_- S_+^{-1} = \begin{pmatrix}
        0 & -1 \\ 1 & 0
    \end{pmatrix},
    \quad
    B = S_+^{-1} S_- = \begin{pmatrix}
        0 & -1 \\
        1 & 1
    \end{pmatrix},
```
ki prav tako generirata $\SL_2(\ZZ)$. Za ti dve matriki velja $A^2 = B^3 = -I$. Kot v končnem primeru lahko tvorimo <span class="definicija">modularno grupo</span>
```{math}
{\textstyle \PSL_2(\ZZ)} = \frac{\SL_2(\ZZ)}{\{ I, -I \}}.
```
Naj bosta $a,b$ sliki matrik $A,B$ v $\PSL_2(\ZZ)$. Velja torej $a^2 = b^3 = 1$. Ker matriki $a,b$ generirata grupo $\PSL_2(\ZZ)$, lahko vsak njen element zapišemo kot besedo s črkama $a$ in $b$. Glavna prednost alternativne izbire generatorjev izhaja iz dejstva, da ima vsak element *enoličen* tak zapis.[^24]

<div class="trditev">

Vsak element v $\PSL_2(\ZZ)$ lahko enolično zapišemo v obliki
```{math}
b^{i_0} a b^{i_1} a \cdots b^{i_{n-1}} a b^{i_n}
```
za nek $n \in \NN_0$ in $i_j \in \{0,1,2 \}$, pri čemer je $i_j \neq 0$ za vsak $j \neq 0,n$.

</div>

<div class="dokaz">

Jasno ima vsak element tak zapis, saj $a,b$ generirata $\PSL_2(\ZZ)$ in velja $a^2 = b^3 = 1$. Preverimo še enoličnost. Predpostavimo, da je $n$ najmanjše število, za katero je izraz kot zgoraj enak $1$.[^25] Seveda je tedaj $n \neq 0$ in kratek račun pokaže tudi, da je $n \neq 1$. Za $n \geq 2$ konjugiramo izraz iz trditve in dobimo
```{math}
1 = a b^{i_1} a b^{i_2} \cdots a b^{i_{n-1}} a b^{i_n + i_0}.
```
Če je $i_n + i_0$ deljivo s $3$, potem je zadnji člen trivialen in po krajšanju $a$ dobimo krajši izraz enake oblike, ki je enak $1$, kar je protislovno z minimalnostjo $n$. Torej $i_n + i_0$ ni deljivo s $3$. To pomeni, da smo $1$ zapisali kot produkt elementov $ab$ in $ab^2$. Dvignimo ta zapis v grupo $\SL_2(\ZZ)$. Izračunamo
```{math}
AB = \begin{pmatrix}
        -1 & -1 \\ 0 & -1
    \end{pmatrix}
    = - S_+, \quad
    AB^2 = \begin{pmatrix}
        -1 & 0 \\ -1 & -1
    \end{pmatrix}
    = - S_-,
```
zato je v $\SL_2(\ZZ)$ neka beseda v $S_+, S_-$ dolžine $n \geq 2$ enaka $\pm I$. To pa je protislovje, saj se pri množenju matrik $S_+, S_-$ vsota vseh koeficientov matrike povečuje, torej zagotovo ne moremo dobiti matrike $\pm I$.

</div>

#### Upodobitve

Namesto upodobitev grupe $\SL_2(\ZZ)$ opazujmo upodobitve nekoliko enostavnejše grupe $\PSL_2(\ZZ)$. Vsak homomorfizem te grupe v katerokoli grupo $G$ je določen s sliko generatorjev $a,b$. Glede na enolično predstavitev elementov grupe $\PSL_2(\ZZ)$ pa je res tudi obratno: za vsako izbiro elementov $X,Y \in G$ z lastnostjo $X^2 = Y^3 = 1$ lahko na enoličen način predpišemo homomorfizem[^26]
```{math}
\textstyle \rho 
    \colon \PSL_2(\ZZ) \to G, \quad
    a \mapsto X, \ b \mapsto Y.
```
Na ta način dobimo mnogo homomorfizmov v različne grupe $G$.

<div class="zgled">

Z GAP se lahko prepričamo, da je alternirajoča grupa $A_9$ generirana s permutacijama
```{math}
(1 \ 4)(2 \ 9)(3 \ 7)(5 \ 6), \quad
    (1 \ 2 \ 3)(4 \ 5 \ 6)(7 \ 8 \ 9).
```
Če torej $a$ preslikamo v prvo permutacijo, $b$ pa v drugo, dobimo surjektivni homomorfizem $\alpha_9 \colon \SL_2(\ZZ) \to A_9$. Splošneje lahko na podoben način konstruiramo surjektivni homomorfizem $\alpha_n$ v grupo $A_n$ za vsak $n \geq 9$.

</div>

<div class="domacanaloga">

Prepričaj se, da za *nobeno* število $N \geq 2$ ne velja, da se homomorfizem $\alpha_9$ faktorizira prek kongruenčnega homomorfizma $\pi_N$. Natančneje, ne obstaja homomorfizem $h \colon \SL_2(\ZZ/N\ZZ) \to A_9$, da bi veljalo $h \circ \pi_N = \alpha_9$. V pomoč ti bo Kitajski izrek o ostankih. Kvocient $A_9$ grupe $\SL_2(\ZZ)$ je v tem smislu *nekongruenčen*.

</div>

Grupa $\SL_2(\ZZ)$ ima torej končne kvociente $\PSL_2(\FF_p)$ in $A_n$, ki tvorijo standardne predstavnike končnih enostavnih grup. Vsaka od teh končnih grup nam da svoje nerazcepne upodobitve, s čimer po restrikciji dobimo mnogo različnih nerazcepnih upodobitev grupe $\SL_2(\ZZ)$. Teorija upodobitev grupe $\SL_2(\ZZ)$ bo torej zajemala bolj ali manj vso kompleksnost teorije upodobitev končnih enostavnih grup. Težko si je predstavljati, kako vse te spraviti pod eno streho.

Obravnave vseh upodobitev se lotimo sistematično po razsežnostih. Vsaka $n$-razsežna kompleksna upodobitev je določena z izbiro matrik $X,Y \in \GL_n(\CC)$ z lastnostjo $X^2 = Y^3 = I$. Upodobitve nas zanimajo le do izomorfizma natančno, kar pomeni, da moramo za razumevanje izomorfnostnih razredov upodobitev razumeti kvocientno množico
```{math}
{\textstyle \Rep_n} = \frac{\{ (X, Y) \in \GL_n(\CC) \times \GL_n(\CC) \mid X^2 = Y^3 = I \}}
    {\GL_n(\CC)},
```
pri čemer grupa $\GL_n(\CC)$ deluje s hkratnim konjugiranjem na parih matrik, se pravi $A \cdot (X,Y) = (A X A^{-1}, A Y A^{-1})$ za $A \in \GL_n(\CC)$.[^27] Elementi množice $\Rep_n$ predstavljajo ravno vse predstavnike izomorfnostnih razredov $n$-razsežnih upodobitev grupe $\PSL_2(\ZZ)$.

Opišimo najprej enorazsežne upodobitve $\Rep_1$. Za števili $X,Y \in \CC^*$ mora veljati $X \in \{1, -1 \}$ in $Y \in \{ 1, \zeta, \zeta^2 \}$, kjer je $\zeta = e^{2 \pi i / 3}$. Delovanje grupe $\CC^*$ na parih je v tem primeru kar trivialno. Velja torej
```{math}
\textstyle \Rep_1 = \{ 1, -1 \} \times \{ 1, \zeta, \zeta^2 \}
```
in imamo $6$ enorazsežnih upodobitev grupe $\PSL_2(\ZZ)$.

Oglejmo si sedaj še dvorazsežne upodobitve $\Rep_2$. Kot bomo videli, je teh *neštevno mnogo*. Sistematično obravnavajmo vse možnosti za matriki $X,Y$.

1.  Če je $X$ ali $Y$ skalarna matrika, potem lahko s konjugiranjem dosežemo, da sta obe matriki hkrati diagonalni. Predpostavimo najprej, da je $X$ skalarna. Zaradi pogoja $X^2 = I$ to pomeni, da je $X = \alpha I$ za $\alpha \in \{ 1, -1 \}$. Po konjugiranju lahko dosežemo, da je $Y$ diagonalna matrika z diagonalnima členoma $a, b \in \{ 1, \zeta, \zeta^2 \}$ (upoštevajoč $Y^3 = I$). Imamo torej dve možnosti za $X$ in šest možnosti za $Y$. Oglejmo si zdaj še možnost, ko je $Y$ skalarna, $X$ pa ni skalarna. To pomeni $Y = \beta I$ za $\beta \in \{ 1, \zeta, \zeta^2 \}$. Po konjugiranju lahko dosežemo, da je $X$ diagonalna matrika z diagonalnima členoma $1, -1$ ($X$ ni skalarna in $X^2 = I$). Imamo torej tri možnosti za $Y$ in eno samo za $X$. Skupaj dobimo $15$ upodobitev. Vse te upodobitve so seveda razcepne.

2.  Če niti $X$ niti $Y$ nista skalarni matriki, potem imata obe dve različni lastni vrednosti. Po konjugiranju lahko matriki $X$, $Y$ zato zapišemo v obliki
    ```{math}
    X = \begin{pmatrix}
                1 & 0 \\ 0 & -1
            \end{pmatrix}, \quad
            Y = \begin{pmatrix}
                a & b \\ c & d
            \end{pmatrix}
    ```
    za neke $a,b,c,d \in \CC$. Centralizator matrike $X$ v $\GL_2(\CC)$ je enak torusu diagonalnih matrik. S temi matrikami lahko torej še dodatno konjugiramo in poenostavimo matriko $Y$. Ločimo več možnosti.[^28]

    1.  Če je $c = 0$ in $b = 0$, potem je $Y$ diagonalna matrika. Njeni lastni vrednosti sta različna tretja korena enote, zato je $Y$ oblike
        ```{math}
        Y = \begin{pmatrix}
                        a & 0 \\ 0 & d
                    \end{pmatrix}
        ```
        za $a,d\in \{ 1, \zeta, \zeta^2 \}$, $a \neq d$. Vse te upodobitve so seveda razcepne. Število vseh je $6$.

    2.  Če je $c = 0$ in $b \neq 0$, potem je $Y$ zgornjetrikotna matrika. Njeni lastni vrednosti sta različna tretja korena enote in z dodatnim konjugiranjem z diagonalno matriko dosežemo, da je $b = 1$, zato je $Y$ oblike
        ```{math}
        Y = \begin{pmatrix}
                        a & 1 \\ 0 & d
                    \end{pmatrix}
        ```
        za $a,d\in \{ 1, \zeta, \zeta^2 \}$, $a \neq d$. Vse te upodobitve so seveda razcepne. Število vseh je $6$.

        Analogno dobimo $6$ razcepnih upodobitev, ko je $c \neq 0$ in $b = 0$.

    3.  Če je $c \neq 0$ in $b \neq 0$, potem z dodatnim konjugiranjem z diagonalno matriko dosežemo, da je $Y$ oblike
        ```{math}
        Y = \begin{pmatrix}
                        a & b \\ 1 & d
                    \end{pmatrix}
        ```
        za $b \in \CC^*$. Pri tem je determinanta te matrike enaka $\delta = ad-b$, sled pa je enaka $\tau = a + d$. Ker sta lastni vrednosti $Y$ različna tretja korena enota, so edine možnosti
        ```{math}
        (\tau, \delta) \in \{ (\zeta + \zeta^2, 1), (1 + \zeta, \zeta), (1 + \zeta^2, \zeta^2) \}.
        ```
        Za vsako od teh možnosti števili $a,d$ določimo kot rešitvi enačbe $\lambda^2 - \tau \lambda + \delta + b = 0$. Če je $b = (\tau^2 - 4 \delta)/4$, dobimo eno samo matriko $Y$, sicer pa imamo dve različni možnosti. Vse te upodobitve so nerazcepne, saj $Y$ v nobenem primeru ne ohranja nobenega od standardnih baznih podprostorov. Vseh teh upodobitev je neštevno mnogo.

Sorodno obravnavo bi lahko izvedli v poljubni razsežnosti.

<div class="posledica">

Grupa $\SL_2(\ZZ)$ ima neštevno mnogo kompleksnih nerazcepnih upodobitev poljubne stopnje, večje od $1$.

</div>

### $\SL_3(\ZZ)$

Oglejmo si še grupo $\SL_3(\ZZ)$ kot zgled *aritmetične mreže višjega ranga*.

#### Prezentacija

Upodobitve $\SL_3(\ZZ)$ bi lahko skušali razumeti na podoben način kot $\SL_2(\ZZ)$. Standardna generatorska množica sestoji iz matrik oblike $T_{ij} = I + E_{ij}$ za $1 \leq i, j \leq 3$, $i \neq j$, kjer je $E_{ij}$ matrika z vnosom $1$ na mestu $(i,j)$ in $0$ sicer. Kot v prejšnjem razdelku pa se zadeve poenostavijo z nestandardno izbiro generatorjev
```{math}
x =
    \begin{pmatrix}
        1 &  0 &  1 \\
        0 & -1 & -1 \\
        0 &  1 &  0
    \end{pmatrix}, \quad
    y =
    \begin{pmatrix}
        0 &  1 &  0 \\
        0 &  0 &  1 \\
        1 &  0 &  0
    \end{pmatrix}, \quad
    z =
    \begin{pmatrix}
        0 &  1 &  0 \\
        1 &  0 &  0 \\
       -1 & -1 & -1
    \end{pmatrix}.
```
Na ta način lahko dobimo precej preprosto <span class="definicija">prezentacijo</span> te grupe, ki je podobna zelo uporabnemu opisu grupe $\PSL_2(\ZZ)$ z generatorjema $a,b$ iz prejšnjega razdelka. Bistvena razlika je, da ta prezentacija vsebuje nekaj pogojev med generatorji $x,y,z$, ki niso tako zelo enostavne oblike kot v grupi $\PSL_2(\ZZ)$. Izkaže se [(Conder-Robertson-Williams 1992)](https://www.ams.org/proc/1992-115-01/S0002-9939-1992-1079696-5/), da vse te pogoje lahko zajamemo z naslednjimi enakostmi:[^29]
```{math}
x^3 = y^3 = z^2 = (xz)^3 = (yz)^3 = (x^{-1}zxy)^2 = (y^{-1}zyx)^2 = (xy)^6 = I.
```
Z drugimi besedami, če želimo podati upodobitev $\SL_3(\ZZ)$ v $\GL_n(\CC)$, potem moramo izbrati matrike $X,Y,Z \in \GL_n(\CC)$, ki zadoščajo vsem tem enakostim. Vsaka taka izbira se enolično razširi do upodobitve, ki preslika $x,y,z$ v $X,Y,Z$.

Če naivno skušamo poiskati matrike v $\GL_2(\CC)$ ali $\GL_3(\CC)$, ki zadoščajo tem enakostim, odkrijemo, da zaradi teh dodatnih restriktivnih pogojev dobimo *bistveno manj* rešitev kot v primeru grupe $\PSL_2(\ZZ)$. Teorija upodobitev grupe $\SL_3(\ZZ)$ je, kot bomo videli, precej bolj strukturirana.

#### Končni kvocienti

Razliko med grupo $\SL_2(\ZZ)$ in $\SL_3(\ZZ)$ lahko jasno vidimo v njunih končnih kvocientih. Kot v dvorazsežnem primeru imamo surjektivne <span class="definicija">kongruenčne homomorfizme</span>
```{math}
\textstyle \pi_N \colon \SL_3(\ZZ) \to \SL_3(\ZZ/N\ZZ).
```
Jedra teh homomorfizmov so <span class="definicija">kongruenčne podgrupe</span>. Izkaže se [(Bass-Lazard-Serre 1964)](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-70/issue-3/Sous-groupes-dindice-fini-dans-SLleft-nZ-right/bams/1183526018.full), da pa tukaj (in v vseh $\SL_m(\ZZ)$ za $m \geq 3$) *ni* nobenih bistveno drugačnih homomorfizmov v končne grupe. Natančneje, vsak homomorfizem $\alpha \colon \SL_3(\ZZ) \to G$ v končno grupo $G$ se faktorizira prek nekega kongruenčnega homomorfizma $\pi_N$. Povedano še drugače, vsaka podgrupa $H \leq \SL_3(\ZZ)$ končnega indeksa vsebuje neko kongruenčno podgrupo. Tej lastnosti grupe $\SL_3(\ZZ)$ rečemo <span class="definicija">lastnost kongruenčnih podgrup</span>.[^30]

Vsak končni kvocient $G$ grupe $\SL_3(\ZZ)$ ima svoje nerazcepne upodobitve, ki jih z restrikcijo potegnemo do nerazcepnih upodobitev grupe $\SL_3(\ZZ)$. Po lastnosti kongruenčnih podgrupe je tak $G$ nujno kvocient $\SL_3(\ZZ/N\ZZ)$ za nek $N$, zato bo dovolj opazovati nerazcepne upodobitve kongruenčnih kvocientov. Če je $N$ praštevilo, te zelo dobro razumemo s tehnikami upodobitev končnih grup. V splošnem iz praštevilske faktorizacije $N = p_1^{k_1} p_2^{k_2} \cdots p_m^{k_m}$ z uporabo Kitajskega izreka o ostankih dobimo
```{math}
\textstyle \SL_3(\ZZ/N\ZZ) \cong \SL_3(\ZZ/p_1^{k_1}\ZZ) \times \SL_3(\ZZ/p_2^{k_2}\ZZ) \times \cdots \times \SL_3(\ZZ/p_m^{k_m}\ZZ).
```
Razumeti moramo torej upodobitve grup $\SL_3(\ZZ/p^k\ZZ)$ za praštevilo $p$ in vse potence $k \geq 1$.

#### $p$-adične grupe

Vse kolobarje $\ZZ/p^k\ZZ$ za $k \geq 1$ lahko opazujemo hkrati, in sicer tako, da jih zložimo v ravno vrsto
```{math}
\cdots \to \ZZ/p^k\ZZ \to \cdots \to \ZZ/p^2\ZZ \to \ZZ/p\ZZ,
```
pri čemer so homomorfizmi $r_k \colon \ZZ/p^k\ZZ \to \ZZ/p^{k-1}\ZZ$ redukcije po modulu $p^{k-1}$. Tvorimo <span class="definicija">inverzno limito</span> te vrste,
```{math}
\textstyle \varprojlim_{k \in \NN} \ZZ/p^k\ZZ
    = \left\{
        (\dots, x_k, \dots, x_2, x_1) \in \prod_{k \in \NN} \ZZ/p^k\ZZ \mid
        \forall k \in \NN \colon \ r_k(x_k) = x_{k-1}
    \right\}.
```
Ker je vsak $\ZZ/p^k\ZZ$ kolobar, je tudi ta limita kolobar. Pravimo mu kolobar <span class="definicija">$p$-adičnih celih števil</span> in ga označimo z $\ZZ_p$. Kolobar celih števil $\ZZ$ se naravno vloži v $\ZZ_p$ s preslikavo $n \mapsto (n)_{k \in \NN}$.

Vse končne kolobarje $\ZZ/p^k\ZZ$ opremimo z diskretno topologijo in njihov produkt s produktno topologijo, tako da je $\ZZ_p$ tudi topološki prostor. Po izreku Tihonova je produkt vseh $\ZZ/p^k\ZZ$ kompakten, $\ZZ_p$ pa tvori zaprto množico v tem produktu, zato je tudi $\ZZ_p$ kompakten topološki prostor.[^31]

Na enak način lahko opazujemo vse grupe $\SL_3(\ZZ/p^k\ZZ)$ hkrati. Zložimo jih v ravno vrsto
```{math}
\textstyle \cdots \to \SL_3(\ZZ/p^k\ZZ) \to \cdots \to \SL_3(\ZZ/p^2\ZZ) \to \SL_3(\ZZ/p\ZZ)
```
s prehodnimi homomorfizmi $r_k \colon \SL_3(\ZZ/p^k\ZZ) \to \SL_3(\ZZ/p^{k-1}\ZZ)$ in tvorimo inverzno limito
```{math}
\textstyle \varprojlim_{k \in \NN} \SL_3(\ZZ/p^k\ZZ)
    = \SL_3(\varprojlim_{k \in \NN} \ZZ/p^k\ZZ)
    = \SL_3(\ZZ_p).
```
Grupa $\SL_3(\ZZ_p)$ podeduje topologijo iz prostora $\ZZ_p^9$, zato je kompaktna topološka grupa. Ta grupa naravno vsebuje $\SL_3(\ZZ)$ in po definiciji je opremljena z zveznimi projekcijami v kongruenčne kvociente
```{math}
\textstyle \widetilde{\pi_{p^k}} \colon \SL_3(\ZZ_p) \to \SL_3(\ZZ/p^k\ZZ)
```
za vsak $k \in \NN$. Ker so končni kvocienti opremljeni z diskretno topologijo, so jedra teh homomorfizmov odprte podgrupe v $\SL_3(\ZZ_p)$. Ko $k$ raste, te podgrupe postajajo vedno manjše.

<div class="trditev">

Podgrupe $\ker \widetilde{\pi_{p^k}}$ za $k \in \NN$ tvorijo bazo okolic enote v $\SL_3(\ZZ_p)$.

</div>

<div class="dokaz">

Naj bo $U$ odprta okolica enote v $\SL_3(\ZZ_p)$. Velja torej $U = \SL_3(\ZZ_p) \cap V$ za neko odprto množico $V$ v produktu vseh $\SL_3(\ZZ/p^k\ZZ)$. Po definiciji produktne topologije množica $V$ vsebuje odprto množico oblike
```{math}
\prod_{k \leq K} 1 \times \prod_{k > K} {\textstyle \SL_3(\ZZ/p^k\ZZ)}.
```
Torej $U$ vsebuje presek te množice z $\SL_3(\ZZ_p)$, kar je natanko $\ker \widetilde{\pi_{p^K}}$.

</div>

Iz te lastnosti je razvidno, da se grupa $\SL_3(\ZZ_p)$ obnaša zelo drugače kot Liejeva grupa $\SL_3(\CC)$.

<div class="domacanaloga">

S pomočjo eksponentne preslikave dokaži, da v grupi $\GL_n(\CC)$ obstaja odprta okolica enote $U$, ki ne vsebuje nobene netrivialne podgrupe.[^32]

</div>

Kljub tej razliki pa je vendarle zelo plodno gledati na $\SL_3(\ZZ_p)$ kot na podgrupo splošne linearne grupe $\GL_3(\QQ_p)$ poljem kvocientov $\QQ_p$ kolobarja $\ZZ_p$ in jo v tej luči obravnavati kot neke vrste Liejevo grupo nad sicer nenavadnim poljem $\QQ_p$. Grupa $\SL_3(\ZZ_p)$ je na ta način poseben primer <span class="definicija">$p$-adične analitične grupe</span>. Razviti je mogoče analogno teorijo Liejevih grup nad $p$-adičnimi števili, ki omogoča, da njihove upodobitve razumemo s pomočjo njihovih prirejenih Liejevih algeber. Na ta način je mogoče izpeljati veliko zanimivih rezultatov o upodobitvah teh grup. Na primer [(Aizenbud-Avni 2015)](https://link.springer.com/article/10.1007/s00222-015-0614-8), obstaja konstanta $C$, da je število nerazcepnih kompleksnih $n$-razsežnih upodobitev grupe $\SL_m(\ZZ_p)$ kvečjemu $C n^{22}$ za vsak $m \geq 3$.

Vse upodobitve kongruenčnih kvocientov grupe $\SL_3(\ZZ)$ lahko torej zajamemo tako, da opazujemo le upodobitve $p$-adične kompaktne grupe $\SL_3(\ZZ_p)$. Prepričajmo se še, da na ta način ne bomo zajeli nič drugih upodobitev.

<div class="trditev">

Vsaka zvezna končno razsežna kompleksna upodobitev grupe $\SL_3(\ZZ_p)$ se faktorizira prek $\widetilde{\pi_{p^k}}$ za nek $k \in \NN$.

</div>

<div class="dokaz">

Naj bo $\rho \colon \SL_3(\ZZ_p) \to \GL_n(\CC)$ zvezna upodobitev. Naj bo $U$ odprta okolica enote v $\GL_n(\CC)$, ki ne vsebuje netrivialnih podgrup. Praslika $\rho^{-1}(U)$ je odprta okolica enote v $\SL_3(\ZZ_p)$, zato vsebuje neko kongruenčno jedro $\ker \widetilde{\pi_{p^k}}$. Slika $\rho(\ker \widetilde{\pi_{p^k}})$ je podgrupa v $U$, zato je trivialna. Jedro $\ker \rho$ torej vsebuje to kongruenčno jedro.

</div>

Nazadnje lahko torej vse upodobitve grupe $\SL_3(\ZZ)$, ki se faktorizirajo prek upodobitev končnih grup, razumemo kot zožitve zveznih upodobitev produktov $p$-adičnih grup po vseh praštevilih $p$, se pravi zveznih upodobitev grupe
```{math}
\prod_{p \in \PP} {\textstyle \SL_3(\ZZ_p)},
```
ki jo označimo kot $\SL_3(\widehat{\ZZ})$.

<div class="domacanaloga">

Postojmo pri skrivnostnem objektu $\widehat{\ZZ}$. Za vsako praštevilo $p$ smo definirali kolobar $\ZZ_p$ kot inverzno limito kolobarjev $\ZZ/p^k\ZZ$ glede na naravne prehodne homomorfizme med temi končnimi kolobarji. Na soroden način definiramo kolobar $\widehat{\ZZ}$ kot inverzno limito končnih kolobarjev $\ZZ/n\ZZ$ za vse $n \in \NN$ glede na naravno prehodne homomorfizme med temi končnimi kolobarji (zdaj ti končni kolobarji niso več zloženi v vrsto, ampak v neko mrežo). Kolobar $\widehat{\ZZ}$ lahko gledamo kot podkolobar produkta $\prod_{n \in \NN} \ZZ/n\ZZ$, opremljenega s produktno topologijo. Kolobar celih števil $\ZZ$ se na naraven način vloži v $\widehat{\ZZ}$.

S pomočjo Kitajskega izreka o ostankih se prepričaj, da imamo izomorfizem kolobarjev $\widehat{\ZZ} \cong \prod_{p \in \PP} \ZZ_p$, ki je hkrati homeomorfizem topoloških prostorov (pri čemer na desni uporabimo produktno topologijo).

Premisli, da so obrnljivi elementi v $\widehat{\ZZ}$ ravno množica $\overline{\PP} \setminus \PP$, kjer smo s simbolom $\overline{\PP}$ označili topološko zaprtje množice vseh praštevil v $\widehat{\ZZ}$.

</div>

#### Nerazcepne upodobitve

Nerazcepne upodobitve grupe $\SL_3(\ZZ)$ lahko konstruiramo s pomočjo nerazcepnih upodobitev grupe $\SL_3(\widehat{\ZZ})$ ali pa kot restrikcijo nerazcepnih upodobitev običajne Liejeve grupe $\SL_3(\CC)$. Te upodobitve lahko tenzorsko množimo med sabo. Neverjetno je, da na ta način dobimo *vse* nerazcepne upodobitve grupe $\SL_3(\ZZ)$. Konceptualno lahko to pojasnimo z naslednjo lastnostjo *dviganja* upodobitev.

<div class="izrek">

Naj bo $\rho \colon \SL_3(\ZZ) \to \GL_n(\CC)$ upodobitev. Tedaj obstaja upodobitev
```{math}
\textstyle \tilde \rho \colon \SL_3(\CC) \times \SL_3(\widehat{\ZZ}) \to \GL_n(\CC),
```
katere zožitev na diagonalno vloženo podgrupo $\SL_3(\ZZ)$ je ravno $\rho$, zožitev na $\SL_3(\CC)$ je polinomska upodobitev, zožitev na $\SL_3(\widehat{\ZZ})$ pa je zvezna upodobitev.

</div>

Izrek sloni na <span class="definicija">Margulisovi superrigidnosti</span> diskretnih podgrup v Liejevih grupah. Za grupo $\SL_3(\ZZ)$ jo lahko izrazimo na naslednji način.

<div class="izrek">

Naj bo $\rho \colon \SL_3(\ZZ) \to \GL_n(\CC)$ upodobitev. Tedaj obstaja polinomska upodobitev $\tilde \rho \colon \SL_3(\CC) \to \GL_n(\CC)$, ki se na nekem kongruenčnem jedru $\ker \pi_{N}$ ujema z $\rho$.

</div>

<div class="dokaz">

Grupa $\SL_3(\ZZ)$ je generirana z matrikami $T_{ij} = I + E_{ij}$ za $i \neq j$. Te matrike niso zelo blizu identitete v $\SL_3(\CC)$, zato jih ne moremo potisniti v Liejevo algebro $\slfrak_3(\CC)$ z logaritmom. Lahko pa vseeno formalno izračunamo njihov logaritem. Ker je $E_{ij}^2 = 0$, je $\log T_{ij} = E_{ij} \in \slfrak_3(\CC)$. Z nekaj računanja se prepričamo, da matrike $E_{ij}$ generirajo Liejevo algebro $\slfrak_3(\CC)$.

Nekaj podobnega lahko naredimo v sliki upodobitve $\rho$. Matrike $\rho(T_{ij})$ so daleč od identitete v $\GL_n(\CC)$. Vsako lahko zapišemo v Jordanski obliki kot produkt diagonalne matrike $\rho(T_{ij})_s$ (*polenostavni del*) in matrike z enicami po diagonali $\rho(T_{ij})_u$ (*unipotentni del*). Za unipotentni del velja $(\rho(T_{ij})_u - I)^n = 0$, zato lahko izračunamo logaritem $\log \rho(T_{ij})_u \in \glfrak_n(\CC)$ z razvojem v končno Taylorjevo vrsto. Z nekaj računanja se prepričamo, da matrike $\log \rho(T_{ij})_u$ generirajo Liejevo algebro $\slfrak_3(\CC)$ znotraj $\glfrak_n(\CC)$.

Obe Liejevi algebri lahko povežemo z Liejevo upodobitvijo $\phi \colon \slfrak_3(\CC) \to \glfrak_n(\CC)$, ki jo definiramo kot $E_{ij} \mapsto \log \rho(T_{ij})_u$. To upodobitev pointegriramo do upodobitve grup $\tilde \rho \colon \SL_3(\CC) \to \GL_n(\CC)$.

Konstrukcija $\tilde \rho$ sloni le na uporabi unipotenih delov $\rho(T_{ij})$. Z nekaj računanja se prepričamo, da za število $N = n!$ velja $\rho(T_{ij})_s^N = I$. Od tod hitro sledi, da na kongruenčnem jedru $\ker \pi_N$ polenostavni del nima vpliva, zato se $\rho$ in $\tilde \rho$ na tem jedru ujemata.

</div>

<div class="domacanaloga">

Oglej si [videoposnetek predavanja](http://www.fields.utoronto.ca/talks/congruence-subgroup-problem-and-boundedness-conditions), kjer Lubotzky z uporabo nekaj osnovnih lastnosti $p$-adičnih analitičnih grup skicira, kako lastnost kongruenčnih podgrup implicira Margulisovo superrigidnost.

</div>

Vsaka upodobitev $\SL_3(\ZZ)$ torej do končnega kvocienta natančno izhaja iz upodobitve $\SL_3(\CC)$. Da pokrijemo še vse možne končne kvociente, upoštevamo še zvezne upodobitve $\SL_3(\widehat{\ZZ})$. Z nekaj truda se da s to intuicijo hitro izpeljati Lubotzkyjev izrek.

<div class="domacanaloga">

Preberi dokaz Lubotzkyjevega izreka v [(Putman)](https://www3.nd.edu/~andyp/notes/RepTheorySLnZ.pdf).

</div>

<div class="posledica">

Nerazcepne končno razsežne kompleksne upodobitve grupe $\SL_3(\ZZ)$ so zožitve tenzorskih produktov nerazcepnih polinomskih upodobitev grupe $\SL_3(\CC)$ in nerazcepnih zveznih upodobitev grupe $\SL_3(\widehat{\ZZ})$.

</div>

V posebnem je vseh nerazcepnih upodobitev $\SL_3(\ZZ)$ le števno mnogo, kar je v ostrem nasprotju z neštevno mnogo upodobitvami $\SL_2(\ZZ)$. Vse povedano se da razširiti na grupe $\SL_m(\ZZ)$ za $m \geq 3$.

[^1]: Če bi želeli obravnavati tudi neskončno razsežne upodobitve na prostoru $V$, bi morali to definicijo nekoliko popraviti. Najprej bi morali zahtevati, da vsak element grupe $G$ deluje kot zvezen linearen operator na $V$, kar ni avtomatično v neskončno razsežnih vektorskih prostorih. Za tem bi morali namesto zveznosti preslikave $\rho$ zahtevati, da je le *šibko zvezna*, kar pomeni, da je preslikava $G \times V \to V$, $(g,v) \mapsto \rho(g) \cdot v$ zvezna.

[^2]: Lahko se celo zgodi, da $f_N$ ne konvergira v *nobeni* točki. Take primere je prvi konstruiral Kolmogorov; glej povzetek [(Chen 1962)](https://projecteuclid.org/journals/proceedings-of-the-japan-academy-series-a-mathematical-sciences/volume-38/issue-6/A-remarkable-divergent-Fourier-series/10.3792/pja/1195523374.full?tab=ArticleLink).

[^3]: Vrsta konvergira le za $|z| < 1$, zato v resnici uporabimo razvoj za $r z$ z $r < 1$, nato pa izlimitiramo $r \to 1$ in vzamemo realni del.

[^4]: Za uvodno seznanitev s teorijo mere se lahko obrneš na [(Magajna 2011)](https://www.fmf.uni-lj.si/sl/zalozba/katalog/46/osnove-teorije-mere/).

[^5]: Dokaz obstoja Haarove mere lahko najdeš v prvem poglavju zapiskov [(Hladnik 2006)](https://users.fmf.uni-lj.si/hladnik/3st/HA.pdf).

[^6]: Za dokaz glej na primer zadnje poglavje zapiskov [(Hladnik 2006)](https://users.fmf.uni-lj.si/hladnik/3st/HA.pdf). Tam najdeš tudi ekspliciten opis nerazcepnih zveznih unitarnih upodobitev grupe $\SU_2(\CC)$. V naslednjem razdelku si bomo pogledali še en drug (bolj geometrijski) način, kako lahko pridemo do teh upodobitev.

[^7]: Podobno kot smo že videli v primeru upodobitev grupe $\RR$. Konkretno za vsak avtomorfizem polja $\CC$ dobimo upodobitev $\SL_2(\CC) \to \SL_2(\CC)$, ki aplicira avtomorfizem po členih matrike. Polje $\CC$ ima *mnogo* divjih avtomorfizmov.

[^8]: <span class="definicija">Linearna algebraična grupa</span> je grupa, ki je hkrati množica skupnih ničel nekih polinomov v prostoru $\CC^n$.

[^9]: Pri $k = 0$ dobimo trivialno upodobitev.

[^10]: Ker je polje $\CC$ algebraično zaprto, tukaj obstaja le en torus.

[^11]: Za splošnejšo obravnavo tangentnih prostorov in odvodov med mnogoterostmi glej zapiske [(Forstnerič 2023)](https://users.fmf.uni-lj.si/forstneric/papers/AMbook.pdf).

[^12]: Ta formula je jasna, če matriko $X$ predstavimo v Jordanovi normalni obliki.

[^13]: Liejev homomorfizem je torej linearna preslikava $\phi \colon L_1 \to L_2$, za katero velja $\phi([x,y]) = [\phi(x), \phi(y)]$ za vsaka $x,y \in L_1$.

[^14]: <span class="definicija">Liejeva spletična</span> med Liejevima upodobitvama $\phi_1, \phi_2$ Liejeve algebre $L$ na prostoru $V$ je linearna preslikava $\alpha \in \End(V)$ z lastnostjo $\alpha(\phi_1(x) \cdot v) = \phi_2(x) \cdot \alpha(v)$ za vsaka $x \in L$, $v \in V$. Kadar najdemo obrnljivo Liejevo spletično, sta upodobitvi <span class="definicija">izomorfni</span>.

[^15]: Liejeva upodobitev $\phi \colon L \to \glfrak_n(\CC)$ je <span class="definicija">nerazcepna</span>, če prostor $\CC^n$ nima nobenih netrivialnih $L$-invariantnih podprostorov.

[^16]: Vektor $v$ torej *potisnemo navzdol* s $F$.

[^17]: Vektor $v_n$ torej *potisnemo navzgor* z $E$.

[^18]: Za vsaki dve izbiri delilnih točk lahko namreč najdemo tretjo izbiro, ki je finejša od obeh. Ta sklep je podoben kot pri definiciji Riemannovega integrala.

[^19]: To je analogno temu, da na kompleksna števila $\CC$ gledamo kot na $\RR^2$.

[^20]: Opazovali bi torej Liejeve homomorfizme $\slfrak_2(\CC) \to \glfrak_n(\CC)$, ki so le $\RR$-linearni.

[^21]: Za celovito obravnavo Liejevih grup se lahko obrneš na zapiske [(Mrčun 2024)](https://users.fmf.uni-lj.si/mrcun/preprints/lg.pdf).

[^22]: Grupa $\SO_3(\RR)$ *ni* enostavno povezana. Homeomorfna je projektivnemu prostoru $\RR P^3$.

[^23]: Poseben primer tega fenomena smo videli v razdelku o upodobitvah grupe $\RR/\ZZ$, kjer smo dokazali, da je vsaka zvezna upodobitev grupe $\RR$ odvedljiva.

[^24]: Rečemo, da je grupa $\PSL_2(\ZZ)$ <span class="definicija">prosti produkt</span> podgrup $\langle a \rangle = \ZZ/2\ZZ$ in $\langle b \rangle = \ZZ/3\ZZ$.

[^25]: Če nek element lahko zapišemo v želeni obliki na dva načina, potem vse črke prenesemo na eno stran enakosti in s tem tudi $1$ zapišemo na netrivialen način v želeni obliki.

[^26]: To je analog razširjanja lokalnega homomorfizma, ki smo ga videli pri grupi $\SL_2(\CC)$. Tam nismo imeli enoličnosti zapisa kot tukaj, zato smo se morali potruditi z dokazovanjem dobre definiranosti razširitve homomorfizma z $U$ na ves $\SL_2(\CC)$. Tukaj to dobimo zastonj.

[^27]: Para matrik $(X,Y)$ in $(X', Y')$ sta torej ekvivalentna, če in samo če za neko matriko $A \in \GL_n(\CC)$ velja $(X,Y) = A \cdot (X', Y')$.

[^28]: Obravnava je analogna razumevanju konjugiranostnih razredov v končni grupi $\GL_2(\FF_p)$, le da je tu nekoliko preprostejša, ker ni nerazcepnega torusa.

[^29]: Rečemo, da je grupa $\SL_3(\ZZ)$ dana s prezentacijo z *generatorji* $x,y,z$ in *relacijami*, ki jih podajajo te enakosti. Glej [Teorijo grup](https://urbanjezernik.github.io/teorija-grup) za podrobnosti glede te konstrukcije in več zgledov.

[^30]: Angleško *congruence subgroup property.*

[^31]: Topologija na $\ZZ_p$ je nekoliko neobičajna. Dobimo namreč popolnoma nepovezan topološki prostor. Predstavljamo si ga lahko kot Cantorjevo množico, kot je prikazano [tukaj](http://roice3.org/padics/).

[^32]: Tej lastnosti pravimo <span class="definicija">brez majhnih podgrup</span>, angleško *no small subgroups*.
