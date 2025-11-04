```{raw} html
<style>
  body { counter-reset: chapter 0 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Temelji teorije upodobitev

V tem poglavju bomo vzpostavili temelje teorije upodobitev. Spoznali bomo koncept upodobitve in si ogledali mnogo primerov. Premislili bomo, kako upodobitve med sabo primerjamo in kako iz danih upodobitev sestavimo nove.

## Osnovni pojmi

### Upodobitve grup

Naj bo $G$ grupa in $V$ vektorski prostor nad poljem $F$. Upodobitev grupe $G$ na prostoru $V$ je delovanje $G$ na množici $V$, ki upošteva dodatno strukturo množice $V$, namreč to, da je vektorski prostor. Natančneje, <span class="definicija">upodobitev</span> (rekli bomo tudi <span class="definicija">linearno delovanje</span>) grupe $G$ na prostoru $V$ je homomorfizem grup
```{math}
\rho \colon G \to \GL(V).
```
Pri tem je $\GL(V)$ grupa vseh obrnljivih linearnih preslikav iz prostora $V$ vase. Razsežnosti prostora $V$ rečemo <span class="definicija">stopnja upodobitve</span> in jo označimo z $\deg(\rho)$.

Ko v prostoru $V$ izberemo bazo in torej izomorfizem $V \cong F^{\deg(\rho)}$, lahko upodobitev $\rho$ enakovredno zapišemo kot homomorfizem
```{math}
\rho \colon G \to \textstyle \GL_{\deg(\rho)}(F)
```
iz grupe $G$ v obrnljive matrike razsežnosti $\deg(\rho)$ nad $F$.

Nad poljem kompleksnih števil $F = \CC$ upodobitvam rečemo <span class="definicija">kompleksne</span>, nad polji karakteristike $p > 0$, na primer $F = \FF_p$,[^1] pa upodobitvam rečemo <span class="definicija">modularne</span>.

Za element $g \in G$ in vektor $v \in V$ rezultat delovanja elementa $g$ na vektorju $v$, se pravi $\rho(g)(v)$, včasih pišemo krajše kot $g \cdot v$ ali kar $gv$.[^2]

<div class="zgled">

- Opazujmo matrično grupo $\GL_2(\CC)$ in vektorski prostor $\CC^2$. Množenje matrik z vektorji podaja upodobitev
  ```{math}
  \textstyle \rho \colon \GL_2(\CC) \to \GL(\CC^2) \equiv \GL_2(\CC), \quad
              A \mapsto \left( v \mapsto A \cdot v \right) \equiv A.
  ```

- Opazujmo grupo realnih števil $\RR^*$ za množenje in vektorski prostor $\CC$. Absolutna vrednost podaja upodobitev
  ```{math}
  |\cdot| \colon \RR^* \to \GL(\CC) = \CC^*, \quad
              x \mapsto |x|.
  ```

- Opazujmo grupo celih števil $\ZZ$ in vektorski prostor $\CC$. Eksponentna funkcija podaja upodobitev
  ```{math}
  \chi \colon \ZZ \to \GL(\CC) = \CC^*, \quad
              x \mapsto e^x.
  ```
  Splošneje imamo za vsak parameter $\alpha \in \CC$ upodobitev
  ```{math}
  \chi_{\alpha} \colon \ZZ \to \GL(\CC) = \CC^*, \quad
              x \mapsto e^{\alpha x}.
  ```

- Opazujmo grupo ostankov $\ZZ/q\ZZ$ za poljubno naravno število $q$. Za vsak parameter $m \in \ZZ/q\ZZ$ imamo upodobitev
  ```{math}
  \chi_m \colon \ZZ/q\ZZ \to \GL(\CC) = \CC^*, \quad
              x + q\ZZ \mapsto e^{2 \pi i mx/q}.
  ```

- Opazujmo diedrsko grupo $D_{2n} = \langle s, r \rangle$, v kateri je $s^2 = 1$, $r^n = 1$ in $s r s = r^{-1}$. Ta grupa izhaja iz simetrij $n$-kotnika v ravnini, s čimer nam ponuja svojo naravno upodobitev $\rho \colon D_{2n} \to \GL(\RR^2) = \GL_2(\RR)$, ki preslika generatorja kot
  ```{math}
  s \mapsto \begin{pmatrix}
                  0 & 1 \\ 1 & 0
              \end{pmatrix}, \quad
              r \mapsto \begin{pmatrix}
                  \cos(2 \pi/n) & - \sin(2 \pi/n) \\
                  \sin(2 \pi/n) & \cos(2 \pi/n)
              \end{pmatrix}.
  ```
  Splošneje imamo za vsak parameter $k \in \ZZ$ upodobitev $\rho_k \colon D_{2n} \to \GL(\RR^2) = \GL_2(\RR)$, ki preslika generatorja kot
  ```{math}
  s \mapsto \begin{pmatrix}
                  0 & 1 \\ 1 & 0
              \end{pmatrix}, \quad
              r \mapsto \begin{pmatrix}
                  \cos(2 \pi k/n) & - \sin(2 \pi k/n) \\
                  \sin(2 \pi k/n) & \cos(2 \pi k/n)
              \end{pmatrix}.
  ```

- Opazujmo grupo ostankov $\ZZ/6\ZZ$ in racionalni vektorski prostor $\QQ^2$. Preslikava
  ```{math}
  \rho \colon \ZZ/6\ZZ \to \GL(\QQ^2) = {\textstyle \GL_2(\QQ)}, \quad
              x + 6 \ZZ \mapsto  \begin{pmatrix}
                  1/2 & 1/8 \\
                  -6 & 1/2 \\
              \end{pmatrix}^x
  ```
  je upodobitev grupe $\ZZ/6\ZZ$. Relevantna matrika je namreč reda $6$.

- Opazujmo ciklično grupo $\ZZ/p\ZZ$ za praštevilo $p$ nad končnim poljem $\FF_p$. Preslikava
  ```{math}
  \rho \colon \ZZ/p\ZZ \to \GL(\FF_p^2) = {\textstyle \GL_2(\FF_p)}, \quad
            x \mapsto \begin{pmatrix}
              1 & x \\ 0 & 1
            \end{pmatrix}
  ```
  podaja modularno upodobitev grupe $\ZZ/p\ZZ$. Relevantna matrika je namreč reda $p$.

- Naj bo $G$ grupa in $V$ vektorski prostor nad poljem $F$. <span class="definicija">Trivialna upodobitev</span> grupe $G$ je homomorfizem
  ```{math}
  \rho \colon G \to \GL(V), \quad
              g \mapsto \textstyle \id_V.
  ```
  Kadar je vektorski prostor $V$ razsežnosti $1$, trivialno upodobitev in vektorski prostor sam označimo kot $\oneone$, v primerih višje razsežnosti pa ju označimo kot $\oneone^{\dim V}$.

- Naj bo $V$ vektorski prostor in naj bo $G$ poljubna podgrupa grupe $\GL(V)$. Tedaj je naravna vložitev $G \to \GL(V)$ upodobitev grupe $G$ na prostoru $V$.

  Za konkreten zgled lahko vzamemo $V = \CC^2$ in $G = \langle \left( \begin{smallmatrix} 1 & 1 \\ 0 & 1 \end{smallmatrix} \right) \rangle \leq \GL(\CC^2)$. Na ta način dobimo upodobitev grupe $G \cong \ZZ$ na prostoru $\CC^2$.

- Naj bo $G$ poljubna grupa, opremljena z delovanjem na neki množici $X$. Naj bo $F[X]$ vektorski prostor z bazo $\{ e_x \}_{x \in X}$. Grupa $G$ deluje na $F[X]$ s homomorfizmom
  ```{math}
  \pi \colon G \to \GL(F[X]), \quad
              g \mapsto \left( e_x \mapsto e_{g \cdot x} \right),
  ```
  kjer je $x \in X$. To delovanje imenujemo <span class="definicija">permutacijska upodobitev</span> grupe $G$ na $F[X]$.

  Za konkreten zgled lahko vzamemo $G = S_n$, ki naravno deluje na množici $X = \{ 1, 2, \dots, n \}$. Na ta način dobimo permutacijsko upodobitev grupe $S_n$ na prostoru $F[\{ 1, 2, \dots, n \}]$ razsežnosti $n$.

- Naj bo $G$ grupa in $F$ polje. Grupa $G$ vselej deluje na sebi s Cayleyjevim delovanjem. Prirejeni permutacijski upodobitvi grupe $G$ na $F[G]$[^3] rečemo <span class="definicija">Cayleyjeva upodobitev</span> grupe $G$ nad $F$. To delovanje označimo z $\pi_{\Cay}$.

- Naj bo $G$ grupa in $F$ polje. Naj bo $\fun(G,F)$ množica vseh funkcij iz množice $G$ v $F$. Te funkcije lahko po točkah seštevamo in množimo s skalarji, na ta način je $\fun(G,F)$ vektorski prostor. Grupa $G$ deluje na $\fun(G,F)$ s homomorfizmom
  ```{math}
  \rho_{\fun} \colon G \to \GL(\fun(G,F)), \quad
              g \mapsto \left( f \mapsto \left( x \mapsto f(xg) \right) \right),
  ```
  kjer je $f \in \fun(G,F), \ x \in G$. To delovanje izhaja iz (desnega) Cayleyjevega delovanja grupe $G$ na sebi in ga zato imenujemo <span class="definicija">(desna) regularna upodobitev</span> grupe $G$ nad $F$.

</div>

Upodobitev $\rho$ grupe $G$ pohvalimo s pridevnikom <span class="definicija">zvesta</span>, kadar je injektivna, se pravi $\ker \rho = 1$. Trivialna upodobitev netrivialne grupe ni zvesta, sta pa vselej zvesti Cayleyjeva in desna regularna upodobitev.

### Kategorija upodobitev

Naj bo $G$ grupa. Opazujmo neki njeni upodobitvi $\rho_1$ in $\rho_2$ nad vektorskima prostoroma $V_1$ in $V_2$, obema nad poljem $F$. Ti dve upodobitvi lahko *primerjamo* med sabo, in sicer tako, da hkrati primerjamo vektorska prostora in delovanji grupe $G$ na teh dveh prostorih.

Natančneje, <span class="definicija">spletična</span>[^4] med upodobitvama $\rho_1$ in $\rho_2$ je linearna preslikava $\Phi \colon V_1 \to V_2$, za katero za vsak $g \in G$ in $v \in V_1$ velja[^5]
```{math}
\Phi(\rho_1(g) \cdot v) = \rho_2(g) \cdot \Phi(v).
```

<div class="zgled">

Opazujmo grupo $\ZZ$ in dve njeni upodobitvi, ki smo ju že videli. Prva naj bo upodobitev
```{math}
\rho \colon \ZZ \to \GL(\CC^2), \quad
    x \mapsto \begin{pmatrix} 1 & x \\ 0 & 1 \end{pmatrix},
```
druga pa naj bo kar trivialna upodobitev $\oneone$ na prostoru $\CC$. Predpišimo linearno preslikavo $\Phi \colon \CC \to \CC^2$ v standardni bazi z matriko $\left( \begin{smallmatrix} 1 \\ 0 \end{smallmatrix} \right)$. Tedaj za vsak vektor $v \in \CC$ in vsako število $x \in \ZZ$ velja
```{math}
\Phi(x \cdot v) 
    =  \begin{pmatrix} xv \\ 0 \end{pmatrix} 
    = x \cdot  \begin{pmatrix} v \\ 0 \end{pmatrix} 
    = x \cdot \Phi(v),
```
zato je $\Phi$ spletična med $\oneone$ in $\rho$.

</div>

Množica vseh spletičen med $\rho_1$ in $\rho_2$ je podmnožica množice linearnih preslikav $\hom(V_1, V_2)$, za katero uporabimo oznako $\hom_G(\rho_1, \rho_2)$ ali kar $\hom_G(V_1, V_2)$.

Za dano upodobitev $\rho$ grupe $G$ na vektorskem prostoru $V$ je identična preslikava $\id_V$ seveda spletična med $\rho$ in $\rho$. Prav tako lahko vsaki dve spletični $\Phi_1$ med $\rho_1$ in $\rho_2$ ter $\Phi_2$ med $\rho_2$ in $\rho_3$ skomponiramo do spletične $\Phi_2 \circ \Phi_1$ med $\rho_1$ in $\rho_3$. Množica vseh upodobitev dane grupe $G$ nad poljem $F$ torej tvori <span class="definicija">kategorijo upodobitev</span>, katere objekti so upodobitve grupe $G$ nad $F$, morfizmi pa so spletične med upodobitvami. To kategorijo označimo z $\Rep_G$.

### Izomorfnost upodobitev

<div class="domacanaloga">

Naj bo $\Phi \colon V_1 \to V_2$ spletična med upodobitvama $\rho_1$ in $\rho_2$, ki je obrnljiva kot linearna preslikava. Prepričaj se, da je tudi njen inverz $\Phi^{-1} \colon V_2 \to V_1$ spletična med $\rho_2$ in $\rho_1$.

</div>

Spletični $\Phi$, ki je obrnljiva kot linearna preslikava, rečemo <span class="definicija">izomorfizem</span> upodobitev $\rho_1$ in $\rho_2$.

<div class="zgled">

Opazujmo ciklično grupo $\ZZ/n\ZZ$ za poljuben $n > 1$. Ta grupa naravno deluje na množici $\Omega = \{ 1, 2, \dots, n \}$,[^6] od koder izhaja permutacijska upodobitev
```{math}
\pi \colon \ZZ/n\ZZ \to \GL(\CC[\Omega]).
```
Grupa $\ZZ/n\ZZ$ ima tudi Cayleyjevo upodobitev,
```{math}
\pi_{\Cay} \colon \ZZ/n\ZZ \to \GL(\CC[\ZZ/n\ZZ]).
```
Ti dve upodobitvi sta izomorfni. Vektorska prostora lahko namreč naravno primerjamo z bijektivno linearno preslikavo
```{math}
\Phi \colon \CC[\Omega] \to \CC[\ZZ/n\ZZ], \quad    
        e_i \mapsto e_{\bar i},
```
kjer je $i \in \Omega$. Preslikava $\Phi$ je spletična, saj za vsak $\bar x \in \ZZ/n\ZZ$ in $i \in \Omega$ velja
```{math}
\Phi(\bar x \cdot e_i) 
        = \Phi(e_{x + i})
        = e_{\overline{x + i}}
        = \bar x \cdot e_{\bar i}
        = \bar x \cdot \Phi(e_i).
```
V to kratko zgodbo lahko vključimo še desno regularno upodobitev
```{math}
\rho_{\fun} \colon \ZZ/n\ZZ \to \GL(\fun(\ZZ/n\ZZ,\CC)).
```
Vektorski prostor $\fun(\ZZ/n\ZZ, \CC)$ lahko na naraven način opremimo z bazo iz karakterističnih funkcij
```{math}
1_{\bar x} \colon \ZZ/n\ZZ \to \CC, \quad
        \bar y \mapsto \begin{cases}
            1 & \bar y = \bar x, \\
            0 & \text{sicer}
        \end{cases}
```
za $\bar x \in \ZZ/n\ZZ$. Predpišimo linearno preslikavo[^7]
```{math}
\Phi^\prime \colon \CC[\ZZ/n\ZZ] \to \fun(\ZZ/n\ZZ, \CC), \quad
        e_{\bar x} \mapsto 1_{- \bar x}.
```
Jasno je $\Phi^\prime$ bijektivna. Preverimo še, da je res spletična. Za vsaka $\bar x, \bar y \in \ZZ/n\ZZ$ velja
```{math}
\Phi^\prime(\bar x \cdot e_{\bar y})
        = \Phi^\prime(e_{\overline{x + y}})
        = 1_{- \overline{x + y}}.
```
Po drugi strani za vsak $\bar z \in \ZZ/n\ZZ$ velja
```{math}
\left( \bar x \cdot \Phi^\prime(e_{\bar y}) \right) (\bar z)
        = \left( \bar x \cdot 1_{- \bar y} \right) (\bar z)
        = 1_{- \bar y}(\bar z + \bar x)
        = \begin{cases}
            1 & \bar z = - \overline{x + y}, \\
            0 & \text{sicer}.
        \end{cases}
```
Torej je res $\Phi^\prime(\bar x \cdot e_{\bar y}) = \bar x \cdot \Phi^\prime(e_{\bar y})$. S tem je $\Phi^\prime$ izomorfizem med Cayleyjevo upodobitvijo in desno regularno upodobitvijo.

</div>

Eden pomembnih ciljev teorije upodobitev je razumeti vse upodobitve dane grupe do izomorfizma natančno. Kasneje bomo spoznali, kako lahko to v določenih[^8] primerih *precej dobro* uresničimo.

## Fundamentalne konstrukcije

Naj bo $\rho$ upodobitev grupe $G$ na prostoru $V$ nad poljem $F$. Premislili bomo, kako lahko prostor, grupo ali polje modificiramo na različne načine in tako dobimo neko drugo, novo upodobitev, oziroma kako lahko dano upodobitev vidimo kot rezultat kakšne od teh fundamentalnih konstrukcij.

### Podupodobitve

Naj bo $G$ grupa z upodobitvijo $\rho \colon G \to \GL(V)$. Denimo, da obstaja vektorski podprostor $W \leq V$, ki je *invarianten* za delovanje grupe $G$, se pravi $g \cdot w \in W$ za vsak $g \in G$, $w \in W$. V tem primeru upodobitev $\rho$ inducira upodobitev $\tilde \rho \colon G \to \GL(W)$ in vložitev vektorskih prostorov $\iota \colon W \to V$ je spletična. Upodobitvi $\tilde \rho$ rečemo <span class="definicija">podupodobitev</span> upodobitve $\rho$.

<div class="zgled">

- Naj bo $n$ naravno število. Opazujmo permutacijsko delovanje grupe $\ZZ/n\ZZ$ na množici $\Omega = \{ 1, 2, \dots, n \}$, ki porodi permutacijsko upodobitev na prostoru $\CC[\Omega]$ z baznimi vektorji $e_i$ za $i \in \Omega$. Naj bo še $e_0 = e_n$.

  Naj bo $\zeta \in \CC$ primitiven $n$-ti koren enote. Za $j \in \Omega$ naj bo
  ```{math}
  f_j = \sum_{i \in \Omega} \zeta^{ij} e_i \in \CC[\Omega].
  ```
  Za vsak $\bar x \in \ZZ/n\ZZ$ velja
  ```{math}
  \bar x \cdot f_j =
          \sum_{i \in \Omega} \zeta^{ij} e_{\overline{x + i}} =
          \sum_{i \in \Omega} \zeta^{(i - \bar x)j} e_{i} =
          \zeta^{-\bar x j} \cdot f_j,
  ```
  zato je vsak podprostor $\CC \cdot f_j \leq \CC[\Omega]$ invarianten za delovanje grupe $\ZZ/n\ZZ$ in podupodobitev na tem podprostoru $\CC \cdot f_j$ je očividno izomorfna upodobitvi $\chi_{-j}$ grupe $\ZZ/n\ZZ$. Na ta način smo sestavili $n$ podupodobitev permutacijske in s tem regularne upodobitve ciklične grupe moči $n$.

- Naj bo $G$ grupa in $\rho$ njena upodobitev na prostoru $V$. Opazujmo množico vseh fiksnih vektorjev te upodobitve,
  ```{math}
  V^G = \{ v \in V \mid \forall g \in G \colon \ g \cdot v = v \}.
  ```
  Množica $V^G$ je vektorski podprostor prostora $V$, ki je invarianten za delovanje grupe $G$. Torej je $\tilde \rho \colon G \to \GL(V^G)$ podupodobitev upodobitve $\rho$. Na prostoru $V^G$ po definiciji grupa $G$ deluje trivialno, torej je $\tilde \rho$ izomorfna trivialni upodobitvi $\oneone^{\dim V^G}$.

  <div class="domacanaloga">

  Naj bo $G$ grupa in $F$ polje. Določi upodobitvi $F[G]^G$ in $\fun(G,F)^G$.

  </div>

  Prostor $V^G$ lahko razumemo še na naslednji alternativen način, ki nam bo prišel zelo prav v nadaljevanju. Iz vsakega vektorja $v \in V^G$ izhaja spletična
  ```{math}
  \Phi_v \colon \oneone \to V, \quad
          x \mapsto x v
  ```
  med $\oneone$ in $\rho$. S tem je določena preslikava $V^G \to \hom_G(\oneone, V)$. Ta preslikava ima jasen inverz, ki spletični $\Phi \in \hom_G(\oneone, V)$ priredi $\Phi(1)$. Na ta način lahko identificiramo prostor $V^G$ z množico spletičen $\hom_G(\oneone, V)$.

- Naj bo $G$ grupa in $\rho$ njena upodobitev na prostoru $V$. Predpostavimo, da obstaja vektor $v \in V$, ki je lastni vektor vsake linearne preslikave $\rho(g)$ za $g \in G$.

  Torej za vsak $g \in G$ obstaja $\chi(g) \in F$, da je $\rho(g) \cdot v = \chi(g) v$. Na ta način dobimo funkcijo $\chi \colon G \to F$, se pravi element prostora $\fun(G,F)$. Ta funkcija ni čisto poljubna; ker je $\rho$ upodobitev, je $\chi$ nujno *homomorfizem* iz grupe $G$ v grupo $F^*$. Torej je $\chi$ pravzaprav upodobitev grupe $G$ na prostoru $F$ razsežnosti $1$.[^9]

  Zdaj kot v zadnjem zgledu s predpisom
  ```{math}
  \Phi \colon F \to V, \quad
          x \mapsto xv
  ```
  dobimo injektivno spletično med $\chi$ in $\rho$, torej lahko vidimo $\chi$ kot enorazsežno podupodobitev upodobitve $\rho$. Hkrati lahko iz te spletične obnovimo podatek o skupnem lastnem vektorju $v$ in upodobitvi $\chi$.[^10]

  Vzpostavili smo torej bijektivno korespondenco med množico enorazsežnih podupodobitev upodobitve $\rho$ in skupnimi lastnimi vektorji vseh preslikav $\rho(g)$ za $g \in G$.

  Poseben primer te korespondence je zadnji zgled. Množico enorazsežnih trivialnih podupodobitev upodobitve $\rho$ lahko identificiramo z množico neničelnih spletičen $\hom_G(\oneone, V) \backslash \{ x \mapsto 0 \}$, ta pa ustreza skupnim lastnim vektorjem $\rho(g)$ za $g \in G$ z lastno vrednostjo $1$, kar je ravno množica $V^G \backslash \{ 0 \}$.

- Naj bo $G$ grupa in $F$ polje. Opazujmo Cayleyjevo upodobitev $\pi_{\Cay}$ na $F[G]$ in desno regularno upodobitev $\rho_{\fun}$ na $\fun(G,F)$. Trdimo, da je $\pi_{\Cay}$ podupodobitev upodobitve $\rho_{\fun}$.

  V ta namen predpišimo linearno preslikavo[^11]
  ```{math}
  \Phi \colon F[G] \to \fun(G,F), \quad
          e_g \mapsto 1_{g^{-1}}
  ```
  za $g \in G$. Jasno je $\Phi$ injektivna preslikava. Hkrati za vse $g,h,x \in G$ velja
  ```{math}
  \Phi(\pi_{\Cay}(g) \cdot e_h) 
          = \Phi(e_{gh})
          = 1_{h^{-1} g^{-1}}
  ```
  in
  ```{math}
  \left( \rho_{\fun}(g) \cdot \Phi(e_h) \right)(x)
          = 1_{h^{-1}}(xg)
          = 1_{h^{-1} g^{-1}}(x),
  ```
  zato je $\Phi$ tudi spletična.

  Kadar je grupa $G$ *končna*, sta prostora $F[G]$ in $\fun(G,F)$ enake razsežnosti, zato sta v tem primeru upodobitvi $\pi_{\Cay}$ in $\rho_{\fun}$ izomorfni. Kadar je grupa $G$ *neskončna*, pa preslikava $\Phi$ vsekakor ni bijektivna.[^12] V tem primeru upodobitvi nista izomorfni.[^13]

</div>

<div class="domacanaloga">

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$. Naj bo $N$ podgrupa edinka v $G$. Premisli, da množica fiksnih točk
```{math}
V^N = \{ v \in V \mid \forall n \in N \colon \ \rho(n) \cdot v = v \}
```
tvori podupodobitev upodobitve $\rho$, ki jo lahko identificiraš z množico $\hom_N(\oneone, V)$.

</div>

### Jedro, slika, kvocient

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$. Ogledali smo si že, kako za vsak $G$-invarianten podprostor $W \leq V$ dobimo podupodobitev upodobitve $\rho$. Sorodno lahko za vsak $G$-invarianten podprostor $W \leq V$ tvorimo <span class="definicija">kvocient</span> $V/W$, na njem linearno deluje grupa $G$ s predpisom
```{math}
G \to \GL(V/W), \quad
    g \mapsto \left( v + W \mapsto \rho(g) \cdot v + W \right)
```
za $v \in V$.

Na vse do zdaj omenjene konstrukcije lahko gledamo na skupen način, in sicer s pomočjo spletične $\Phi$, ki vlaga prostor $W$ v $V$. Ni težko preveriti, da so standardne konstrukcije, ki jih lahko uporabimo na spletičnah vektorskih prostorov, na naraven način opremljene z linearnim delovanjem grupe $G$.

<div class="trditev">

Naj bo $\Phi$ spletična upodobitev grupe $G$. Tedaj prostori $\ker \Phi$, $\image \Phi$, $\mathrm{coker} \; \Phi$ podedujejo linearno delovanje grupe $G$.

</div>

<div class="zgled">

Naj bo $G$ grupa in $\rho$ njena upodobitev na prostoru $V$. Podprostor prostora $V$, na katerem grupa $G$ deluje trivialno, je vselej $G$-invarianten. Največji tak podprostor je ravno prostor vseh fiksnih vektorjev $V^G$. Videli smo že, da lahko ta prostor identificiramo z množico spletičen $\hom_G(\oneone, V)$.

Oglejmo si sedaj še dual zgodnje konstrukcije. Naj bo $V_1 = \langle \rho(g) \cdot v - v \mid v \in V, \ g \in G \rangle$. Prostor $V_1$ je $G$-invarianten podprostor prostora $V$, zato kvocient $V/V_1$ podeduje linearno delovanje grupe $G$. Po konstrukciji je to delovanje trivialno in prostor $V/V_1$ je največji kvocient prostora $V$, na katerem grupa $G$ deluje trivialno. Kvocient $V/V_1$ označimo z $V_G$ in mu pravimo <span class="definicija">prostor koinvariant</span> upodobitve $\rho$.

<div class="domacanaloga">

Izračunaj prostor koinvariant regularne upodobitve ciklične grupe $\ZZ/n\ZZ$.

</div>

Prostor koinvariant je po konstrukciji dualen prostoru fiksnih vektorjev, zato lahko nanj prenesemo tudi interpretacijo s spletičnami. Opazujmo množico $\hom_G(V, \oneone)$. Spletične iz te množice so ravno linearne preslikave $\lambda \colon V \to F$ z lastnostjo $\lambda(\rho(g) \cdot v) = \lambda(v)$ za vsaka $v \in V, \ g \in G$, kar je ekvivalentno pogoju $\lambda(V_1) = 0$. Vsako tako spletično lahko zato interpretiramo kot linearno preslikavo iz $V/V_1 = V_G$ v $F$. Na ta način je vzpostavljena bijektivna korespondenca med množico spletičen $\hom_G(V,\oneone)$ in množico linearnih preslikav $\hom_F(V_G, F)$, slednja množica pa je ravno dual $V_G^*$ prostora koinvariant $V_G$.

</div>

### Direktna vsota

Naj ima grupa $G$ družino upodobitev $\{ \rho_i \}_{i \in I}$ na vektorskih prostorih $\{ V_i \}_{i \in I}$. Tedaj lahko tvorimo direktno vsoto vektorskih prostorov $\bigoplus_{i \in I} V_i$, ki je opremljena z linearnim delovanjem
```{math}
\bigoplus_{i \in I} \rho_i \colon G \to \GL(\bigoplus_{i \in I} V_i), \quad
  g \mapsto \left( \sum_{i \in I} v_i \mapsto \sum_{i \in I} \rho_i(g) \cdot v_i \right).
```
Na ta način dobimo <span class="definicija">direktno vsoto</span> upodobitev $\bigoplus_{i \in I} \rho_i$. Pri tem je vsaka od upodobitev $\rho_i$ podupodobitev te direktne vsote.

<div class="zgled">

- Opazujmo permutacijsko upodobitev $\pi$ grupe $\ZZ/n\ZZ$ na prostoru $\CC[\Omega]$, kjer je $\Omega = \{ 1, 2, \dots, n \}$. Premislili smo že, da ima ta upodobitev $n$ podupodobitev. Za vsak $j \in \Omega$ imamo upodobitev na podprostoru $\CC \cdot f_j$, ki je izomorfna upodobitvi $\chi_{-j}$. Ker je množica vektorjev $\{ f_j \mid j \in \Omega \}$ linearno neodvisna,[^14] lahko permutacijsko upodobitev torej zapišemo kot direktno vsoto $\pi = \bigoplus_{j \in \Omega} \chi_j$.

  <div class="domacanaloga">

  Prepričaj se, da so upodobitve $\chi_j$ za $j \in \Omega$ grupe $\ZZ/n\ZZ$ med sabo paroma neizomorfne.

  </div>

- Opazujmo permutacijsko upodobitev simetrične grupe $S_3$ na prostoru $\RR[\{ 1,2,3 \}] = \RR^3$. Delovanje grupe $S_3$ ohranja vektor $e_1 + e_2 + e_3$, zato ima ta upodobitev trivialno enorazsežno podupodobitev, dano s podprostorom $\langle e_1 + e_2 + e_3 \rangle$. Eden od komplementov tega podprostora je $\langle e_1 - e_2, e_2 - e_3 \rangle$, ki je hkrati $S_3$-invariaten podprostor.[^15] Če označimo $u_1 = e_1 - e_2$ in $u_2 = e_2 - e_3$, lahko slednjo upodobitev opišemo s homomorfizmom
  ```{math}
  \rho \colon S_3 \to \GL(\langle u_1, u_2 \rangle), \quad
          (1 \ 2) \mapsto \begin{pmatrix} 
              -1 & 1 \\ 0 & 1 
          \end{pmatrix}, \quad
          (1 \ 2 \ 3) \mapsto \begin{pmatrix} 
              0 & -1 \\ 1 & -1
          \end{pmatrix}.
  ```
  Permutacijska upodobitev $S_3$ je zato direktna vsota enorazsežne podupodobitve $\oneone$ in dvorazsežne podupodobitve $\rho$.

  Premislimo, da upodobitve $\rho$ *ne* moremo zapisati kot direktne vsote svojih pravih podupodobitev. V ta namen opazujmo njene morebitne enorazsežne podupodobitve. Premislili smo že, da te ustrezajo skupnim lastnim vektorjem vseh preslikav $\rho(x)$ za $x \in S_3$. Lastna vektorja $\rho((1 \ 2))$ sta $u_1$ in $u_1 + 2 u_2$. Noben od teh dveh vektorjev ni hkrati lastni vektor $\rho((1 \ 2 \ 3))$. Torej je upodobitev $\rho$ stopnje $2$, hkrati pa nima enorazsežnih podupodobitev in je torej ne moremo nadalje razstaviti.

</div>

Direktna vsota je najbolj preprost način, kako lahko iz danih upodobitev sestavimo novo upodobitev. V nadaljevanju bomo zato veliko časa posvetili obratnemu problemu: dano upodobitev bomo kot v zadnjem zgledu skušali razstaviti na direktno vsoto čim bolj enostavnih podupodobitev.

### Tenzorski produkt

Naj ima grupa $G$ upodobitvi $\rho_1$ in $\rho_2$ na prostorih $V_1$ in $V_2$. Tedaj lahko tvorimo <span class="definicija">tenzorski produkt</span> vektorskih prostorov $V_1 \otimes V_2$, ki je naravno opremljen z linearnim delovanjem
```{math}
\rho_1 \otimes \rho_2 \colon G \to \GL(V_1 \otimes V_2), \quad
    g \mapsto \left( v_1 \otimes v_2 \mapsto \rho_1(g) v_1 \otimes \rho_2(g) v_2 \right).
```

<div class="domacanaloga">

Izberimo bazi prostorov $V_1$ in $V_2$. Tenzorski produkti baznih elementov tvorijo bazo prostora $V_1 \otimes V_2$. Kako izgleda matrika $(\rho_1 \otimes \rho_2)(g)$ v odvisnosti od matrik $\rho_1(g)$ in $\rho_2(g)$?

</div>

<div class="zgled">

Opazujmo simetrično grupo $S_3$. Ogledali smo si že njeno permutacijsko upodobitev na prostoru $\RR^3$, ki smo jo razstavili na direktno vsoto trivialne upodobitve $\oneone$ in dvorazsežne upodobitve $\rho$. Poleg teh dveh ima grupa $S_3$ še eno zanimivo upodobitev, ki izračuna predznak dane permutacije, se pravi
```{math}
\sgn \colon S_3 \to \GL(\RR) = \RR^*, \quad
    \sigma \mapsto \sgn(\sigma).
```
To je netrivialna enorazsežna upodobitev.

Tvorimo tenzorski produkt upodobitev $\rho$ in $\sgn$. Dobimo upodobitev na vektorskem prostoru $\RR \otimes \RR^2$, ki ga lahko naravno identificiramo s prostorom $\RR^2$. V tem smislu je upodobitev $\sgn \otimes \rho$ izomorfna dvorazsežni upodobitvi
```{math}
S_3 \to \GL(\RR^2), \quad
    \sigma \mapsto \left( v \mapsto \sgn(\sigma) \cdot \rho(\sigma) \cdot v \right).
```

<div class="domacanaloga">

Dokaži, da sta upodobitvi $\rho$ in $\sgn \otimes \rho$ izomorfni.

</div>

</div>

Naj ima grupa $G$ upodobitev na prostoru $V$. Tedaj lahko tvorimo <span class="definicija">tenzorske potence</span> $V^{\otimes n}$ za $n \in \NN_0$. Vsaka od teh tvori upodobitev grupe $G$. Na prostoru $V^{\otimes n}$ deluje simetrična grupa $S_n$, in sicer na dva načina. Prvi način izhaja iz permutacijske upodobitve grupe $S_n$, in sicer dobimo delovanje
```{math}
\pi \colon S_n \to \GL(V^{\otimes n}), \quad
    \sigma \mapsto \left( v_1 \otimes v_2 \otimes \cdots \otimes v_n \mapsto  v_{\sigma(1)} \otimes v_{\sigma(2)} \otimes \cdots \otimes v_{\sigma(n)} \right).
```
Drugi način delovanja grupe $S_n$ na tenzorski potenci pa je $\sgn \otimes \pi$, pri katerem delovanje $\pi$ še utežimo s predznakom delujoče permutacije. Prostor koinvariant upodobitve $\pi$ je
```{math}
{\textstyle \Sym^n(V)} =
    \frac{V^{\otimes n}}{
        \left\langle v_1 \otimes v_2 \otimes \cdots \otimes v_n -  v_{\sigma(1)} \otimes v_{\sigma(2)} \otimes \cdots \otimes v_{\sigma(n)} \mid v_i \in V, \ \sigma \in S_n \right\rangle
    },
```
imenujemo ga <span class="definicija">simetrična potenca</span> upodobitve $G$ na $V$. Analogno prostor koinvariant upodobitve $\sgn \otimes \pi$ označimo z $\bigwedge^n(V)$ in imenujemo <span class="definicija">alternirajoča potenca</span>. Obe potenci sta seveda upodobitvi grupe $G$. Vse potence hkrati zajamemo z direktnima vsotama
```{math}
\textstyle \Sym(V) = \bigoplus_{n \in \NN_0} \Sym^n(V) 
    \quad \text{in} \quad
    \bigwedge V = \bigoplus_{n \in \NN_0} \textstyle\bigwedge^n(V).
```

<div class="domacanaloga">

Naj bo $G$ grupa s kompleksno upodobitvijo $\rho$ na prostoru $V$ razsežnosti $\deg(\rho) < \infty$. Dokaži, da je upodobitev $G$ na alternirajoči potenci $\bigwedge^{\deg(\rho)} V$ izomorfna enorazsežni upodobitvi $G \to \CC^*, \ g \mapsto \det(\rho(g))$.

</div>

### Dual

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$ nad poljem $F$. Tvorimo lahko <span class="definicija">dualen prostor</span> $V^* = \hom(V, F)$, ki je naravno opremljen z linearnim delovanjem
```{math}
\rho^* \colon G \to \GL(V^*), \quad
    g \mapsto \left( \lambda \mapsto \left( v \mapsto \lambda(\rho(g^{-1}) \cdot v) \right) \right)
```
za $\lambda \in V^*, \ v \in V$. Na ta način dobimo <span class="definicija">dualno upodobitev</span> $\rho^*$ upodobitve $\rho$.

Za funkcional $\lambda \in V^*$ in vektor $v \in V$ včasih uporabimo oznako $\langle \lambda, v \rangle$ za aplikacijo $\lambda(v)$. S to oznako lahko zapišemo definicijo dualne upodobitve kot
```{math}
\langle \rho^*(g) \cdot \lambda, v \rangle = \langle \lambda, \rho(g^{-1}) \cdot v \rangle.
```

<div class="zgled">

Opazujmo grupo $\ZZ$ in za parameter $a \in \CC$ njeno upodobitev
```{math}
\chi_a \colon \ZZ \to \GL(\CC), \quad
    x \mapsto e^{ax}.
```
Za dualno upodobitev $\chi_a^*$, funkcional $\lambda \in \CC^*$ in vektor $z \in \CC$ velja
```{math}
\langle \chi_a^*(x) \cdot \lambda, z \rangle = 
    \langle \lambda, \chi_a(-x) \cdot z \rangle =
    \lambda(e^{-ax} \cdot z).
```
Funkcionali v dualnem prostoru $\CC^*$ so skalarna množenja s kompleksnimi števili. Če funkcionalu $\lambda$ ustreza število $l \in \CC$, dobimo torej
```{math}
\chi_a^*(x) \cdot l = e^{-ax} \cdot l.
```
Dualna upodobitev $\chi_a^*$ je torej enorazsežna upodobitev, ki je izomorfna upodobitvi $\chi_{-a}$.

</div>

<div class="domacanaloga">

- Naj bosta $\rho_1, \rho_2$ upodobitvi grupe $G$. Dokaži, da je
  ```{math}
  \left( \rho_1 \oplus \rho_2 \right)^* \cong \rho_1^* \oplus \rho_2^*
          \quad \text{in} \quad
          \left( \rho_1 \otimes \rho_2 \right)^* \cong \rho_1^* \otimes \rho_2^*.
  ```

- Naj bo $\rho$ upodobitev grupe $G$ z $\deg(\rho) < \infty$. Tedaj je $\left( \rho^* \right)^* \cong \rho$.

</div>

Naj bo zdaj $G$ grupa z dvema upodobitvama $\rho$ in $\sigma$ na prostorih $V$ in $W$. <span class="definicija">Prostor linearnih preslikav</span> $\hom(V,W)$ je naravno opremljen z linearnim delovanjem
```{math}
\hom(\rho, \sigma) \colon G \to \GL(\hom(V,W)), \quad
    g \mapsto \left( \Phi \mapsto \left( v \mapsto \sigma(g) \cdot \Phi \cdot \rho(g^{-1}) \cdot v \right) \right).
```
Invariante tega delovanja sestojijo iz linearnih preslikav, ki so invariantne glede na predpisano delovanje grupe $G$, se pravi ravno iz spletičen med $\rho$ in $\sigma$. S simboli je torej $\hom(V,W)^G = \hom_G(V,W)$.

<div class="trditev">

Naj bo $G$ grupa z upodobitvama $\rho$ in $\sigma$. Predpostavimo, da je $\deg(\sigma) < \infty$. Tedaj je $\hom(\rho, \sigma) \cong \rho^* \otimes \sigma$.

</div>

<div class="dokaz">

Naj bo $\rho$ upodobitev na prostoru $V$ in $\sigma$ upodobitev na prostoru $W$. Izomorfizem med vektorskima prostoroma $V^* \otimes W$ in $\hom(V,W)$ podaja linearna preslikava
```{math}
V^* \otimes W \to \hom(V,W), \quad
    \lambda \otimes w \mapsto \left( v \mapsto \lambda(v) \cdot w \right).
```
Ni težko preveriti, da je ta preslikava spletična.

</div>

### Skalarji

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$ nad poljem $F$. Naj bo $E$ razširitev polja $F$. Tedaj je prostor $E \otimes V$ naravno opremljen z linearnim delovanjem
```{math}
E \otimes \rho \colon G \to \GL(E \otimes V), \quad
    g \mapsto \left( e \otimes v \mapsto e  \otimes \rho(g) \cdot v \right).
```
Ta postopek konstrukcije prostora $E \otimes V$ imenujemo <span class="definicija">razširitev skalarjev</span>. Dano upodobitev lahko razširimo do ugodnejših skalarjev[^16], lahko pa tudi dano upodobitev nad velikim poljem $E$ gledamo kot razširitev skalarjev neke upodobitve nad preprostejšim poljem $F$.[^17] V tem slednjem primeru rečemo, da je dana upodobitev <span class="definicija">definirana nad poljem</span> $F$. Včasih nam uspe najti celo preprost *podkolobar* polja $F$, nad katerim je definirana dana upodobitev.

<div class="zgled">

Opazujmo grupo $S_3$ in njeno permutacijsko upodobitev na realnem prostoru $\RR[\{ 1, 2, 3 \}]$. Poznamo že njeno dvorazsežno upodobitev $\rho$ na podprostoru $\langle e_1 - e_2, e_2 - e_3 \rangle$, ki *nima* enorazsežnih podupodobitev. Ta je definirana z matrikami, ki imajo zgolj celoštevilske koeficiente. Upodobitev $\rho$ je zato definirana nad *kolobarjem* $\ZZ$. To upodobitev lahko zato *projiciramo* s homomorfizmom kolobarjev $\ZZ \to \ZZ/p\ZZ$ za poljubno praštevilo $p$ do upodobitve
```{math}
S_3 \to {\textstyle \GL_2(\ZZ/p\ZZ)}, \quad
    (1 \ 2) \mapsto \begin{pmatrix} 
        -1 & 1 \\ 0 & 1 
    \end{pmatrix}, \quad
    (1 \ 2 \ 3) \mapsto \begin{pmatrix} 
        0 & -1 \\ 1 & -1
    \end{pmatrix},
```
ki je definirana nad *končnim* poljem $\ZZ/p\ZZ$. Pri $p = 3$ ima ta projicirana upodobitev enorazsežen invarianten podprostor $\langle e_1 + e_2 + e_3 \rangle$. Projekcije nam lahko torej dano upodobitev dodatno razstavijo.

</div>

Kadar imamo opravka s konkretnim poljem $F$, lahko dano upodobitev modificiramo tudi z <span class="definicija">avtomorfizmi polja</span>. Te si najlažje predstavljamo po izbiri baze vektorskega prostora. Če je $\sigma \in \Aut(F)$, dobimo iz dane upodobitve $\rho \colon G \to \GL_n(F)$ modificirano upodobitev
```{math}
\rho^\sigma \colon G \to {\textstyle \GL_n(F)}, \quad
    g \mapsto \rho(g)^\sigma,
```
pri kateri vsak člen matrike $\rho(g)$ preslikamo z avtomorfizmom $\sigma$.

<div class="zgled">

Naj bo $G$ grupa s kompleksno upodobitvijo $\rho$. Kompleksno konjugiranje je avtomorfizem polja $\CC$, zato lahko s konjugiranjem členov matrik tvorimo <span class="definicija">konjugirano upodobitev</span> $\overline{\rho}$.

</div>

### Restrikcija

Naj bo $G$ grupa z upodobitvijo $\rho \colon G \to \GL(V)$. Kadar je na voljo še ena grupa $H$ s homomorfizmom $\phi \colon H \to G$, lahko upodobitev $\rho$ sklopimo s $\phi$ in dobimo upodobitev $\rho \circ \phi$ grupe $H$ na prostoru $V$. Temu postopku pridobivanja upodobitev grupe $H$ iz upodobitev grupe $G$ pravimo <span class="definicija">restrikcija</span>, pri tem pa novo upodobitev $\rho \circ \phi$ označimo kot $\Res^G_H(\rho)$. Predstavljamo si, da smo upodobitev $\rho$ *potegnili nazaj* vzdolž homomorfizma $\phi$. Restrikcija je funktor iz kategorije $\Rep_G$ v kategorijo $\Rep_H$.

<div class="zgled">

Naj bo $G$ grupa s podgrupo edinko $N$. Tvorimo kvocientni homomorfizem $\phi \colon G \to G/N$. Vsaki upodobitvi grupe $G/N$ lahko z restrikcijo priredimo upodobitev grupe $G$. Vsaka taka pridobljena upodobitev grupe $G$ vsebuje podgrupo $N$ v svojem jedru. Na ta način dobimo bijektivno korespondenco med upodobitvami grupe $G/N$ in upodobitvami grupe $G$, ki so trivialne na $N$.

Običajno ni res, da je vsaka upodobitev grupe $G$ trivialna na $N$, se pa to lahko zgodi v kakšnih posebnih primerih. Na primer, *enorazsežne* upodobitve grupe $G$ nad poljem $F$ so homomorfizmi iz $G$ v $F^*$, kar ravno ustreza homomorfizmom iz abelove grupe $G/[G,G]$ v $F^*$. Vsaka enorazsežna upodobitev grupe $G$ je torej trivialna na $[G,G]$.

Za konkreten primer si oglejmo simetrično grupo $S_n$. Njene kompleksne enorazsežne upodobitve ustrezajo homomorfizmom $S_n \to \CC^*$. Ker je $[S_n, S_n] = A_n$, opazujemo torej homomorfizme $S_n/A_n \cong \ZZ/2\ZZ \to \CC^*$. Na voljo sta le dva taka homomorfizma: trivialen in netrivialen (ki preslika generator grupe $\ZZ/2\ZZ$ v $-1 \in \CC^*$). Prvi ustreza trivialni upodobitvi $\oneone$, drugi pa ustreza predznačni upodobitvi $\sgn$.

</div>

Kadar imamo na voljo tri grupe, povezane s homomorfizmoma $\phi_2 \colon H_2 \to H_1$ in $\phi_1 \colon H_1 \to G$, lahko restrikcijo izvedemo dvakrat zaporedoma. Upodobitvi $\rho$ v $\Rep_G$ tako priredimo upodobitev $\Res^{H_1}_{H_2}(\Res^G_{H_1}(\rho))$ v $\Rep_{H_2}$. Od grupe $H_2$ do $G$ imamo neposredno povezavo prek homomorfizma $\phi_1 \circ \phi_2$, s čimer dobimo upodobitev $\Res^G_{H_2}(\rho)$. Ni težko preveriti, da sta dobljeni upodobitvi izomorfni. Tej lastnosti restrikcije pravimo <span class="definicija">tranzitivnost</span>.

### Indukcija

Naj bo kot zgoraj $G$ grupa in $H$ še ena grupa s homomorfizmom $\phi \colon H \to G$. <span class="definicija">Indukcija</span> je postopek, ki s pomočjo homomorfizma $\phi$ upodobitvi $\rho$ grupe $H$ priredi upodobitev grupe $G$. Indukcija torej deluje ravno v obratno smer kot restrikcija in nam omogoča, da upodobitev $\rho$ *potisnemo naprej* vzdolž homomorfizma $\phi$. Ta postopek je nekoliko bolj zapleten kot restrikcija.

Začnimo z upodobitvijo $\rho \colon H \to \GL(V)$. Konstruirali bomo prostor, na katerem deluje grupa $G$. Odskočna deska za to bo regularna upodobitev grupe $G$, katere vektorski prostor je prostor funkcij $\fun(G,F)$. Ta prostor razširimo s prostorom $V$ do prostora funkcij
```{math}
\fun(G,V) = \{ f \mid f \colon G \to V \},
```
na katerem linearno deluje grupa $G$ z analogom regularne upodobitve, in sicer kot
```{math}
g \cdot f = \left( x \mapsto f(xg) \right)
```
za $g \in G, \ f \in \fun(G,V)$. Po drugi strani na tej množici deluje tudi grupa $H$, in sicer na dva načina: prvič prek homomorfizma $\phi$ in pravkar opisanega delovanja grupe $G$, drugič pa prek svojega delovanja $\rho$ na prostoru $V$. Ko ti dve delovanji združimo, dobimo delovanje grupe $H$ na prostoru funkcij $\fun(G,V)$ s predpisom
```{math}
h \cdot f = \left( x \mapsto \rho(h) \cdot f \left( \phi(h^{-1}) \cdot x \right) \right)
```
za $h \in H, \ f \in \fun(G,V)$.[^18] Opazujmo invariantni podprostor
```{math}
\fun(G, V)^H =
    \left\{ f \in \fun(G,V) \mid \forall h \in H, x \in G. \ \rho(h) \cdot f(x) = f \left(\phi(h) \cdot x\right)\right\}.
```
Ker grupa $G$ deluje na $\fun(G,V)$ prek množenja z *desne*, pogoj pripadnosti invariantam $\fun(G,V)^H$ pa je izražen prek množenja z *leve*, je podprostor $\fun(G,V)^H$ avtomatično $G$-invarianten. S tem smo dobili upodobitev grupe $G$ na prostoru $\fun(G,V)^H$. To je želena <span class="definicija">inducirana upodobitev</span>. Zanjo uporabimo oznako $\Ind^G_H(\rho)$.

<div class="zgled">

Naj bo $G$ grupa z vložitvijo $\phi \colon 1 \to G$ trivialne podgrupe. Vsaka upodobitev trivialne grupe nad poljem $F$ je trivialna. Iz enorazsežne trivialne upodobitve $\oneone$ dobimo prostor funkcij $\fun(G,F)$, na katerem grupa $G$ deluje z regularno upodobitvijo. Inducirana upodobitev je v tem primeru torej kar regularna, se pravi $\Ind^G_1(\oneone) = \rho_{\fun}$.

</div>

Inducirano upodobitev $\Ind^G_H(\rho) = \fun(G,V)^H$ smo konstruirali z invariantami grupe $H$. To pomeni, da vektorji v tem prostoru niso poljubne funkcije v $\fun(G,V)$, temveč zadoščajo določenim restriktivnim pogojem. Te funkcije so določene z vrednostmi, ki jih zavzamejo na predstavnikih desnih odsekov $\image \phi \backslash G$,[^19] in te vrednosti pripadajo podprostoru $V^{\ker \phi}$.[^20]

<div class="zgled">

Naj bo $G$ grupa z upodobitvijo $\rho$ in naj bo $\phi = \id_G$. Tedaj je vsaka funkcija $f \in \fun(G,V)^G$ določena že z vrednostjo $f(1)$. Dodatnih restrikcij za to vrednost ni, zato dobimo izomorfizem vektorskih prostorov
```{math}
\fun(G,V)^G \to V, \quad
        f \mapsto f(1),
```
ki je spletična glede na regularno delovanje $G$ na $\fun(G,V)$. S tem imamo torej izomorfizem upodobitev $\Ind^G_G(\rho) \cong \rho$.

</div>

<div class="domacanaloga">

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$ in naj bo $\phi \colon G \to G/N$ kvocientna projekcija za neko podgrupo edinko $N$ v $G$. Dokaži, da je $\Ind^{G/N}_G(\rho)$ izomorfna upodobitvi $G/N$ na prostoru $V^N$, ki izhaja iz upodobitve $\rho$.

</div>

Najpomembnejši primer indukcije, čeravno ne tudi najbolj preprost, je <span class="definicija">indukcija iz podgrupe končnega indeksa</span>. Naj bo $G$ grupa s podgrupo $H$ in naj bo $\phi$ vložitev $H$ v $G$. Predpostavimo, da je $|G:H| < \infty$. Naj bo $\rho$ upodobitev grupe $H$ na prostoru $V$. Premislimo, kako izgleda upodobitev $\Ind^G_H(\rho)$.

Naj bo $R$ neka izbrana množica predstavnikov desnih odsekov $H$ v $G$. Vsaka funkcija $f \in \fun(G,V)^H$ je določena z vrednostmi $f(r)$ za $r \in R$ in dodatnih restrikcij za te vrednosti ni, zato dobimo izomorfizem vektorskih prostorov[^21]
```{math}
\Phi \colon \fun(G,V)^H \to \fun(R,V), \quad
        f \mapsto \left( r \mapsto f(r) \right).
```
Da dobimo spletično, moramo posplošitev regularnega delovanja $G$ na $\fun(G,V)$ prenesti prek linearnega izomorfizma $\Phi$ na desno stran. V ta namen naj bo $v \in V$ in $f \in \fun(G,V)^H$ z lastnostjo $f(r_0) = v$ in $f(r) = 0$ za $r \in R \backslash \{ r_0 \}$. Za vsak $g \in G$ mora tako veljati
```{math}
g \cdot \left( r \mapsto \begin{cases} v & r = r_0, \\ 0 & r \neq r_0 \end{cases} \right) =
        \Phi \left( g \cdot f \right) =
        \Phi \left( x \mapsto f(xg) \right).
```
Za $x \in R$ z lastnostjo $xg \in Hr_0$, se pravi $x = h r_0 g^{-1}$ za nek $h \in H$, velja $f(xg) = f(hr_0) = \rho(h) \cdot v$. Seveda je $|R \cap H r g^{-1}| = 1$, torej obstaja natanko en tak $x$. Za $x \in R$ z lastnostjo $xg \notin Hr_0$ pa velja $f(xg) = 0$. S tem je
```{math}
g \cdot \left( r \mapsto \begin{cases} v & r = r_0, \\ 0 & r \neq r_0 \end{cases} \right) =
        \left( r \mapsto \begin{cases} \rho(h) \cdot v & r = h r_0 g^{-1} \text{ za nek $h \in H$,} \\ 0 & r \notin H r_0 g^{-1} \end{cases} \right).
```
Da bo preslikava $\Phi$ spletična, moramo na $\fun(R,V)$ torej uvesti tako delovanje grupe $G$, ki dan vektor $v$ pri vnosu $r_0 \in R$ preslika tako, da najprej izračuna odsek elementa $r_0 g^{-1}$ po $H$, ta element zapiše kot $r_0 g^{-1} = h^{-1} r$ za $h \in H, \ r \in R$, nato pa na vektor $v$ deluje z $\rho(h)$ in ga hkrati prestavi k vnosu $r$.

Opisan postopek si lahko nekoliko lažje predstavljamo tako, da množico $\fun(R,V)$ identificiramo z direktno vsoto $\bigoplus_{r \in R} V r$, kjer je $Vr$ kopija vektorskega prostora $V$ pri komponenti $r$. Element $g \in G$ deluje na vektorju $v r_0 \in Vr_0$ kot $g^{-1}$ z desne. V teh domačih oznakah izračunamo
```{math}
g \cdot v r_0 = v r_0 g^{-1} = v h^{-1} r = (h \cdot v) r = (\rho(h) \cdot v) r,
```
kar ravno ustreza bolj zakompliciranemu zapisu zgoraj.

Poseben primer opisane indukcije dobimo z enorazsežnimi upodobitvami grupe $H$. Vsak homomorfizem $\rho \colon H \to F^*$ porodi prostor $\fun(G,F)^H$ razsežnosti $|G:H|$, ki je podprostor prostora funkcij $\fun(G,F)$ in na katerem torej grupa $G$ deluje z regularno upodobitvijo. Inducirana upodobitev je v tem primeru podupodobitev regularne upodobitve $\rho_{\fun}$. Na ta način lahko dobimo mnogo različnih upodobitev grupe $G$.

<div class="zgled">

Opazujmo grupo $S_n$ in njeno podgrupo $A_n$ indeksa $2$. Za $n \geq 5$ je grupa $A_n$ enostavna, zato je $A_n = [A_n, A_n]$ in ni netrivialnih enorazsežnih upodobitev. Oglejmo si inducirano upodobitev $\Ind^{S_n}_{A_n}(\oneone)$. A priori vemo, da je to dvorazsežna upodobitev. Za množico predstavnikov odsekov vzamemo $R = \{ (), (1 \ 2) \}$. V domačih oznakah je vektorski prostor upodobitve enak $F ()\oplus F (1 \ 2)$, na katerem deluje grupa $S_n$ s predpisom
```{math}
g \cdot x \sigma = x \sigma g^{-1} = \begin{cases}
            x \sigma   & g \in A_n, \\
            x \left((1 \ 2)\sigma\right)    & g \notin A_n
        \end{cases}
```
za $g \in S_n, \ x \in F, \ \sigma \in R$. To delovanje lahko zapišemo še enostavneje. Vektorski prostor identificiramo z dvorazsežnim prostorom $F^2$, delovanje pa opišemo kot
```{math}
g \cdot \begin{pmatrix}
            x \\ y
        \end{pmatrix} =
        \begin{cases}
            \begin{pmatrix}
                x \\ y
            \end{pmatrix} & g \in A_n, \\
            \begin{pmatrix}
                y \\ x
            \end{pmatrix} & g \notin A_n
        \end{cases}
```
za $x,y \in F, \ g \in S_n$. Alternirajoča grupa $A_n$ je v jedru te upodobitve, ki zato izhaja iz kvocienta $S_n/A_n \cong \ZZ/2\ZZ$. Opisana upodobitev je natanko permutacijska upodobitev grupe $\ZZ/2\ZZ$ na prostoru $F[\{ 1, 2 \}]$, inducirana upodobitev pa je ravno restrikcija te upodobitve vzdolž kvocientne projekcije $S_n \to S_n/A_n$. Inducirano upodobitev lahko zapišemo kot vsoto dveh enorazsežnih podupodobitev. Prva je podupodobitev z diagonalnim prostorom $\{ (x,x) \mid x \in F \} \leq F^2$, ta je izomorfna trivialni upodobitvi $\oneone$. Druga pa je podupodobitev z antidiagonalnim prostorom $\{ (x, -x) \mid x \in F \} \leq F^2$. Ta ni trivialna, saj element $(1 \ 2)$ deluje na $(1, -1)$ kot množenje z $-1 \in F$. Ta podupodobitev je zato izomorfna predznačni upodobitvi $\sgn$. Nazadnje je torej $\Ind^{S_n}_{A_n}(\oneone) \cong \oneone \oplus \sgn$.

</div>

Naj bosta $G,H$ grupi s homomorfizmom $\phi \colon H \to G$. Ni težko preveriti, da indukcija naravno prenese spletično med dvema upodobitvama grupe $H$ v spletično med induciranima upodobitvama. Indukcija je torej funktor iz kategorije $\Rep_H$ v kategorijo $\Rep_G$.

Kadar imamo na voljo tri grupe, povezane s homomorfizmoma $\phi_2 \colon H_2 \to H_1$ in $\phi_1 \colon H_1 \to G$, lahko indukcijo izvedemo dvakrat zaporedoma. Upodobitvi $\rho$ v $\Rep_{H_2}$ tako priredimo upodobitev $\Ind^{G}_{H_1}(\Ind^{H_1}_{H_2}(\rho))$ v $\Rep_{G}$. Od grupe $H_2$ do $G$ imamo neposredno povezavo prek homomorfizma $\phi_1 \circ \phi_2$, s čimer dobimo upodobitev $\Ind^G_{H_2}(\rho)$. Ni težko preveriti, da sta dobljeni upodobitvi izomorfni. Tej lastnosti indukcije pravimo <span class="definicija">tranzitivnost</span>.

<div class="domacanaloga">

Dokaži tranzitivnost indukcije.

</div>

S tranzitivnostjo indukcije lahko vsako indukcijo vzdolž homomorfizma $\phi \colon H \to G$ razdelimo na tri korake: najprej induciramo vzdolž kvocientne projekcije $H \to H/\ker \phi$, nato vzdolž izomorfizma $H/\ker \phi \to \image \phi$ in nazadnje vzdolž vložitve $\image \phi \to G$. Vsako od teh posameznih indukcij razumemo precej dobro in zato lahko to znanje uporabimo pri razumevanju indukcije vzdolž $\phi$. Na primer, iz povedanega in razmislekov o preprostejših indukcijah, ki smo jih že naredili, sledi, da je razsežnost inducirane upodobitve $\rho$ grupe $H$ na prostoru $V$ enaka
```{math}
\textstyle \deg(\Ind^G_H(\rho)) = 
    |G:\image \phi| \cdot \dim(V^{\ker \phi}).
```

### Adjunkcija restrikcije in indukcije

Indukcija in restrikcija vsekakor nista inverzna funktorja. Na primer, če je $H \leq G$ in $\phi$ vložitev, potem za upodobitev $\rho$ v $\Rep_G$ velja $\deg(\Res^G_H(\rho)) = \deg(\rho)$ in zato $\deg(\Ind^G_H(\Res^G_H(\rho))) = |G:H| \cdot \deg(\rho)$, kar je lahko mnogo večje od $\deg(\rho)$. Sta pa funktorja restrikcije in indukcije vendarle tesno povezana. Tvorita namreč <span class="definicija">adjungiran par</span> funktorjev.[^22]

<div class="trditev">

Naj bosta $G,H$ grupi s homomorfizmom $\phi \colon H \to G$. Za vsako upodobitev $\rho$ v $\Rep_G$ in upodobitev $\sigma$ v $\Rep_H$ velja
```{math}
\textstyle \hom_H(\Res^G_H(\rho), \sigma) \cong 
        \hom_G(\rho, \Ind^G_H(\sigma)).
```

</div>

<div class="dokaz">

Naj bo $\rho$ upodobitev na prostoru $V$ in $\sigma$ upodobitev na prostoru $W$. Naj bo
```{math}
\textstyle \Phi \in \hom_H(\Res^G_H(\rho), \sigma) = \hom_H(V, W).
```
Sestavimo pripadajočo spletično
```{math}
\textstyle \Psi \in \hom_G(\rho, \Ind^G_H(\sigma)) = \hom_G(V, \fun(G,W)^H).
```
Za vektor $v \in V$ definirajmo
```{math}
\Psi(v) = \left( x \mapsto \Phi(\rho(x) \cdot v) \right) \in \fun(G,W).
```

<div class="domacanaloga">

Preveri, da prirejanje $\Phi \mapsto \Psi$ vzpostavi izomorfizem med prostoroma spletičen $\hom_H(V,W)$ in $\hom_G(V,\fun(G,W)^H)$.

</div>

</div>

<div class="zgled">

Naj bo $G$ grupa s podgrupo $H$ končnega indeksa. Grupa $G$ deluje na množici desnih odsekov $H \backslash G$ s homomorfizmom
```{math}
G \to \Sym(H \backslash G), \quad
    g \mapsto \left( Hx \mapsto Hxg^{-1} \right).
```
Iz tega delovanja izhaja permutacijska upodobitev $\pi$ grupe $G$ na prostoru $F[H \backslash G]$. Po konstrukciji je $\pi \cong \Ind^G_H(\oneone)$. Iz adjunkcije med restrikcijo in indukcijo za trivialni upodobitvi grup $G$ in $H$ od tod izpeljemo izomorfizem
```{math}
\hom_H(\oneone, \oneone) \cong \hom_G(\oneone, \pi) \cong F[H \backslash G]^G.
```
Prostor $\hom_H(\oneone, \oneone) = \hom(F,F)$ sestoji zgolj iz skalarnih množenj in je torej enorazsežen. Zato je enorazsežen tudi prostor invariant $F[H \backslash G]^G$. Vektor, ki ga razpenja, lahko dobimo kot sliko $\id_F \in \hom_H(\oneone, \oneone)$. Tej spletični po adjunkciji ustreza spletična
```{math}
\Psi \colon F \to F[H \backslash G], \quad
    1 \mapsto \sum_{Hx \in H \backslash G} e_{Hx},
```
od koder sledi
```{math}
F[H \backslash G]^G = \left\langle \sum_{Hx \in H \backslash G} e_{Hx} \right\rangle.
```

</div>

<div class="domacanaloga">

Naj bosta $G,H$ grupi s homomorfizmom $\phi \colon H \to G$. Za vsako upodobitev $\rho$ v $\Rep_G$ in upodobitev $\sigma$ v $\Rep_H$ velja
```{math}
\textstyle \Ind^G_H(\Res^G_H(\rho) \otimes \sigma) \cong
        \rho \otimes \Ind^G_H(\sigma).
```

</div>

<div class="domacanaloga">

Premisli, kako se restrikcija in indukcija ujameta z dualom, direktno vsoto in tenzorskim produktom.

</div>

[^1]: Končno polje ostankov celih števil pri deljenju s $p$ bomo označili s $\FF_p$.

[^2]: Ta zapis odraža dejstvo, da je upodobitev pravzaprav delovanje grupe $G$ na množici $V$ z dodatnimi lastnostmi. Za vse $g, h \in G$ in $v \in V$ velja $g \cdot (h \cdot v) = (gh) \cdot v$, ker gre za delovanje grupe. Po drugi strani pa za vse $g,h \in G$, $v,w \in V$ in $\alpha \in F$ velja še $g \cdot (v + w) = g \cdot v + g \cdot w$ in $g \cdot (\alpha v) = \alpha (g \cdot v)$, ker je delovanje linearno.

[^3]: Prostor $F[G]$ je vektorski prostor nad $F$, generiran z množico $G$. Običajno mu pravimo <span class="definicija">grupna algebra</span>, saj ta prostor na naraven način podeduje operacijo množenja iz grupe $G$.

[^4]: Angleško *intertwiner*. Simpatičen prevod je po Francetu Križaniču.

[^5]: Z opustitvijo eksplicitnih oznak za delovanja lahko ta pogoj pišemo krajše kot $\Phi(gv) = g\Phi(v)$.

[^6]: Generator $\bar 1 = 1 + n\ZZ \in \ZZ/n\ZZ$ deluje kot cikel $(1 \ 2 \ \cdots \ n)$.

[^7]: Pozor, karakteristična funkcija je zasidrana pri *inverzu* elementa $\bar x$ v $\ZZ/n\ZZ$.

[^8]: Na primer, *precej dobro* bomo opisali upodobitve poljubne končne grupe nad poljem kompleksnih števil.

[^9]: Kadar je $\chi(g) = 1$ za vsak $g \in G$, je ta upodobitev izomorfna $\oneone$. Kadar je $\chi(g) \neq 1$ za vsaj kak $g \in G$, pa ta upodobitev *ni* trivialna.

[^10]: Namreč, $v = \Phi(1)$ in $\chi(g) = \rho(g) \cdot 1$.

[^11]: Poseben primer te preslikave smo videli za grupo $\ZZ/n\ZZ$, kjer smo premislili, da je celo bijektivna.

[^12]: Slika $\image \Phi$ namreč sestoji iz funkcij, ki so neničelne le v končno mnogo elementih grupe $G$.

[^13]: To sledi na primer iz dejstva, da prostora $F[G]^G$ in $\fun(G,F)^G$ nista izomorfna.

[^14]: Prehodna matrika iz baze $e_i$ v bazo $f_j$ je ravno Vandermondova matrika.

[^15]: Na primer, generator $(1 \ 3 \ 2)$ preslika vektor $e_1 - e_2$ v $e_3 - e_1$, kar lahko zapišemo kot $-(e_1 - e_2) - (e_2 - e_3)$.

[^16]: Na primer polja kompleksnih števil.

[^17]: Na primer $E = \CC$ in $F = \QQ$.

[^18]: Delovanje $H$ na $\fun(G,V)$ je konstruirano analogno delovanju grupe na prostoru linearnih preslikav.

[^19]: Če je $R$ množica predstavnikov desnih odsekov $\image \phi$ v $G$ in če že poznamo vrednosti $f \in \fun(G,V)$ na množici $R$, potem lahko vsako drugo vrednost $f$ izračunamo kot $f(x \cdot r) = \rho(y) \cdot f(r)$ za $x = \phi(y) \in \image \phi$.

[^20]: Če je $f \in \fun(G,V)^H$, potem pogoj $H$-invariantnosti uporabimo z elementi $h \in \ker \phi$ in dobimo $\rho(h) \cdot f(x) = f(x)$, torej je $f \in V^h$.

[^21]: Množico funkcij $\fun(R,V)$ lahko vidimo kot direktno vsoto prostorov $V$, indeksirano z množico $R$.

[^22]: V nadaljevanju bomo spoznali presenetljivo uporabnost tega navidez naključnega dejstva.
