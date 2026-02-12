```{raw} html
<style>
  body { counter-reset: chapter 3 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Razširjeni zgledi – končni

Kategorijo upodobitev dane končne grupe nad ugodnim poljem razumemo, če imamo na voljo tabelo karakterjev, izračun te pa je končen problem. S tem smo za konkretne končne grupe dosegli ultimativen cilj teorije upodobitev. Biti pa moramo previdni, da zaradi vseh teh čudovitih dreves ne spregledamo gozda. Grupe namreč praviloma ne nastopajo posamično, temveč kot del večjih družin.[^1] V tem poglavju si bomo podrobneje pogledali dve temeljni družini grup, in sicer simetrične grupe ter splošne linearne grupe nad končnim poljem.[^2] Njuno teorijo upodobitev bomo obravnavali celostno.

## Simetrične grupe

Opazujmo simetrično grupo $S_n$ za $n \in \NN$ nad poljem $\CC$. Ogledali smo si že tabele karakterjev za $n \leq 4$ in razložili, da je število nerazcepnih upodobitev enako številu konjugiranostnih razredov, to pa je enako številu razčlenitev $p(n)$. Družina simetričnih grup je posebna, saj zanjo presenetljivo obstaja eksplicitna korespondenca med konjugiranostnimi razredi in nerazcepnimi upodobitvami. Iz dane razčlenitve $(\lambda_1, \lambda_2, \dots, \lambda_k)$ števila $n$ lahko torej konstruiramo nerazcepno upodobitev grupe $S_n$ in za tem z nekoliko več truda določimo vrednosti karakterjev.

### Nerazcepne upodobitve

Naj bo $\lambda = (\lambda_1, \lambda_2, \dots, \lambda_k)$ razčlenitev $n$. Nerazcepno upodobitev grupe $S_n$, prirejeno $\lambda$, kot ponavadi iščemo z indukcijo iz podgrup. Razčlenitev $\lambda$ lahko interpretiramo kot ciklični tip permutacij, zato se naravno ponuja <span class="definicija">Youngova grupa</span>
```{math}
P = S_{\lambda_1} \times S_{\lambda_2} \times \cdots \times S_{\lambda_k}.
```
Razčlenitev $\lambda$ si lahko predstavljamo kot zaporedje vrstic diagrama, v katerem je $\lambda_1$ škatlic v $1$. vrstici, $\lambda_2$ škatlic v $2$. vrstici, …, $\lambda_k$ škatlic v $k$. vrstici. Pri tem so vrstice poravnane na levo. Takemu shematičnemu prikazu razčlenitve pravimo <span class="definicija">Youngov diagram</span>. Diagram ima $n$ škatlic, v katere poljubno vpišemo števila od $1$ do $n$. Tako izpolnjenemu diagramu pravimo <span class="definicija">Youngova tabela</span>. Vsaka Youngova tabela nam pravzaprav ponuja vložitev grupe $P$ v $S_n$. Fiksirajmo standardno vložitev, ki ustreza temu, da v škatlice vpišemo po vrsti števila od $1$ do $n$, začenši zgoraj levo in hodeč po $1$. vrstici, nato po $2$. vrstici in tako naprej. Grupa $P$, standardno vložena v $S_n$, predstavlja ravno vse permutacije, ki ohranjajo *vrstice* tabele.

<figure>
<img src="img/img_young.png" />
<figcaption>Youngov diagram razčlenitve <span class="math inline"><em>λ</em> = (5, 3, 1)</span> in dve Youngovi tabeli. Druga tabela je standardna.</figcaption>
</figure>

Inducirajmo trivialno upodobitev iz $P$ na $S_n$. V razdelku o indukciji smo spoznali, da lahko $\Ind^{S_n}_{P}(\oneone)$ interpretiramo kot permutacijsko upodobitev $S_n$ na desnih odsekih podgrupe $P$. To interpretacijo lahko vložimo v prostor funkcij $\fun(S_n, \CC)$. Namesto množice $P$ lahko namreč opazujemo indikatorsko funkcijo $1_P$. Element $g \in S_n$ na njej deluje kot $\rho_{\fun}(g) \cdot 1_P = 1_{P g^{-1}}$, se pravi kot permutacija desnih odsekov. Na ta način upodobitveni prostor upodobitve $\Ind^{S_n}_{P}(\oneone)$ vidimo kot
```{math}
\langle \rho_{\fun}(g) \cdot 1_{P} \mid g \in S_n \rangle.
```
Ta prostor lahko izrazimo s pomočjo Fourierove transformacije kot
```{math}
\langle \hat{f}(\rho_{\fun}) \cdot 1_P \mid f \in \fun(S_n, \CC) \rangle
    = \image \Fcal(1_P)
    = \langle 1_P * f \mid f \in \fun(S_n, \CC) \rangle.
```
Upodobitev $S_n$ na tem prostoru gotovo *ni* nerazcepna, saj na primer vsebuje trivialno z večkratnostjo $\langle \chi_{\oneone}, \Ind^{S_n}_{P}(\chi_{\oneone}) \rangle = \langle \chi_{\oneone}, \chi_{\oneone} \rangle = 1$. Ta prostor bomo zato še dodatno projicirali na nek podprostor.

Do zdaj smo upoštevali le grupo $P$ permutacij, ki ohranjajo *vrstice* izbrane Youngove tabele. Iz tega gledišča je naravno, da obravnavamo tudi grupo permutacij, ki ohranjajo *stolpce* tabele. Označimo jo s $Q$. Ravno ta podgrupa je dodatek, ki nam bo dodatno reduciral zgoraj opisano inducirano upodobitev. Pri tem bomo upoštevali, da je $Q$ sestavljena dualno $P$, zato jo bomo utežili s predznačno upodobitvijo $\sgn$.

Definirajmo funkcijo
```{math}
\youngsym = (\sgn \cdot 1_Q) * 1_P \in \fun(S_n, \CC),
```
ki ji pravimo <span class="definicija">Youngov simetrizator</span>. Njene vrednosti so
```{math}
\youngsym(x) = \sum_{p \in P, q \in Q \colon qp = x} \sgn(q).
```
Ker velja $P \cap Q = 1$, ima vsak element $x \in S_n$ *kvečjemu en* zapis v obliki $x = qp$ za $p \in P, q \in Q$,[^3] torej ima zadnja vsota kvečjemu en neničeln člen in je torej enaka karakteristični funkciji množice $QP = \{ qp \mid q \in Q, p \in P \}$, uteženi s predznakom člena v $Q$.

Vzdolž Youngovega simetrizatorja dobimo endospletično $\Fcal(\youngsym)$ regularne upodobitve, katere slika je vektorski prostor
```{math}
V_{\lambda} = \image \Fcal(\youngsym) = \langle \youngsym * f \mid f \in \fun(S_n, \CC) \rangle,
```
ki ga imenujemo <span class="definicija">Spechtov modul</span>. Na tem prostoru naravno deluje grupa $S_n$[^4], dobljeno upodobitev označimo z $\rho_{\lambda}$. Velja $V_{\lambda} \neq 0$, saj je $\youngsym = \youngsym * 1_1 \in V_{\lambda}$.

<div class="izrek">

(o nerazcepnih upodobitvah simetrične grupe)

1.  Za vsako razčlenitev $\lambda$ je $\rho_{\lambda}$ nerazcepna.

2.  Za različni razčlenitvi $\lambda, \mu$ je $\rho_{\lambda} \not\cong \rho_{\mu}$.

3.  Vsaka nerazcepna upodobitev simetrične grupe je izomorfna $\rho_{\lambda}$ za neko razčlenitev $\lambda$.

</div>

Zadnja točka seveda sledi iz prvih dveh, saj je število nerazcepnih upodobitev ravno enako številu razčlenitev $n$. Pred dokazom izreka si oglejmo nekaj zgledov.

<div class="zgled">

- Naj bo $\lambda = (n)$. Tedaj je $P = S_n$ in $Q = 1$, zato je $\youngsym = 1$. Za funkcijo $f \in \fun(S_n, \CC)$ je $\Fcal(1) \cdot f = 1 * f = |G| \cdot \EE(f)$ in grupa $S_n$ deluje trivialno na tej funkciji. S tem je
  ```{math}
  V_{\lambda} = \image \Fcal(1) = \CC
  ```
  in dobimo trivialno upodobitev.

- Naj bo $\lambda = (1,1,\dots,1)$. Tedaj je $P = 1$ in $Q = S_n$, zato je $\youngsym = \sgn$. Za funkcijo $f \in \fun(S_n, \CC)$ je
  ```{math}
  \Fcal(\sgn) \cdot f = \sgn * f = \left( x \mapsto \sum_{g \in G} \sgn(xg^{-1}) f(g) \right) = (\sgn * f)(1) \cdot \sgn,
  ```
  zato je
  ```{math}
  V_{\lambda} = \image \Fcal(\sgn) = \langle \sgn \rangle.
  ```
  Na funkciji $\sgn$ grupa $S_n$ deluje kot $\rho_{\fun}(g) \cdot \sgn = \sgn(g) \cdot \sgn$, torej je $\rho_{\lambda}$ predznačna upodobitev.

- Naj bo $\lambda = (n-1,1)$. Tedaj je $P = S_{n-1}$ in $Q = \{ (), (1 \ n)\}$. Za funkcijo $f \in \fun(S_n, \CC)$ velja najprej
  ```{math}
  \left( 1_P * f \right) (x) = \sum_{p \in P} f(p^{-1} x) = \sum_{g \in Px} f(g),
  ```
  torej $1_P * f$ izračuna vsoto funkcije $f$ po odseku $Px$. Prostor $\image \Fcal(1_P)$ lahko zato identificiramo s podprostorom funkcij $\fun_{P \backslash S_n}(S_n, \CC)$, ki so konstantne na desnih odsekih $P \backslash S_n$. Delovanje $S_n$ na tem prostoru ni nič drugega kot $\Ind^{S_n}_P(\oneone)$, kar prepoznamo kot standardno permutacijsko upodobitev grupe $S_n$ njenega delovanja na $\{ 1, 2, \dots, n \}$. Uporabimo zdaj še konvolucijo s funkcijo $\sgn \cdot 1_Q$. Dobimo linearno preslikavo
  ```{math}
  \textstyle \fun_{P \backslash S_n}(S_n, \CC) \to \fun_{P \backslash S_n}(S_n, \CC), \quad
          \psi \mapsto \left( x \mapsto \psi(x) - \psi((1 \ n) \cdot x) \right).
  ```
  Njeno jedro sestoji iz funkcij $\psi$, ki so konstantne na odsekih $P \backslash S_n$ in povrhu zadoščajo še enakosti $\psi(x) = \psi((1 \ n) \cdot x)$ za vsak $x \in S_n$. Ko ta pogoj uporabimo s transpozicijami $(i \ n)$ za $1 \leq i < n$, sklenemo, da je vsaka taka funkcija $\psi$ nujno konstantna. Nazadnje je torej
  ```{math}
  V_{\lambda} = \image \Fcal(\youngsym) \cong \frac{\textstyle \fun_{P \backslash S_n}(S_n, \CC)}{\CC}.
  ```
  Ta prostor je razsežnosti $n-1$. Prirejeno upodobitev imenujemo <span class="definicija">standardna upodobitev</span> simetrične grupe $S_n$. Kot smo videli, jo lahko dobimo tako, da iz standardne permutacijske upodobitve odstranimo trivialno upodobitev.

</div>

<div class="domacanaloga">

Naj bo $\lambda$ razčlenitev $n$ in $\lambda^\prime$ razčlenitev, ki jo iz $\lambda$ dobimo tako, da transponiramo Youngov diagram. Preveri, da velja $\sgn \otimes \rho_{\lambda} \cong \rho_{\lambda^\prime}$.

</div>

Dokaz izreka bomo izpeljali s pomočjo naslednje leme, v kateri igra ključno vlogo delovanje Fourierove transformacije Youngovega simetrizatorja $\widehat{\youngsym}(\rho_{\fun})$ na prostoru $V_{\lambda}$. V lemi uporabljamo leksikografsko delno urejenost $<$ na množici vseh razčlenitev.

<div class="lema">

Opazujmo simetrično grupo $S_n$.

1.  Za vsako razčlenitev $\lambda$ je $\widehat{\youngsym}(\rho_{\fun}) \cdot V_{\lambda} \subseteq \CC \cdot \youngsym$.

2.  Za razčlenitvi $\lambda > \mu$ je $\widehat{\youngsym}(\rho_{\fun}) \cdot V_{\mu} = 0$.

</div>

<div class="dokaz">

(dokaz izreka o nerazcepnih upodobitvah simetrične grupe)

1.  Naj bo $W \leq V_{\lambda}$ podupodobitev. Po lemi je $\widehat{\youngsym}(\rho_{\fun}) \cdot W$ bodisi $\CC \cdot \youngsym$ bodisi $0$.

    V prvem primeru sledi, da je $\youngsym \in W$, od koder sklenemo $W \geq \langle \rho_{\fun}(g) \cdot \sigma_\lambda \mid g \in S_n \rangle$, kar je ravno enako $\image \Fcal(\youngsym) = V_{\lambda}$.

    Privzemimo zdaj, da je $\widehat{\youngsym}(\rho_{\fun}) \cdot W = 0$, kar lahko zapišemo kot $W * \youngsym = 0$. Od tod sledi $W * V_{\lambda} = 0$ in zato $W * W = 0$. Naj bo $W = \image P$ za neko projektorsko endospletično $P$ regularne upodobitve. Vemo že, da so vse take preslikave oblike $P = \Fcal(w)$ za neko funkcijo $w \in \fun(S_n, \CC)$. Ker je $P \cdot 1_1 = \widehat{1_1}(\rho_{\fun}) \cdot w = w$, sledi $w \in W$. Še več, ker je $P^2 = P$, izračunamo $w = P \cdot w = \widehat{w}(\rho_{\fun}) \cdot w = w * w$. Ker je $W * W = 0$, sledi $w = 0$ in s tem $W = 0$.

2.  Za različni razčlenitvi $\lambda$, $\mu$ lahko brez škode predpostavimo $\lambda > \mu$, saj je $<$ linearna urejenost. Po lemi je $\widehat{\youngsym}(\rho_{\fun}) \cdot V_{\mu} = 0$. Hkrati je $\widehat{\youngsym}(\rho_{\fun}) \cdot V_{\lambda}$ bodisi $\CC \cdot \youngsym$ bodisi $0$. V slednjem primeru pristopimo kot zgoraj: velja $V_{\lambda} * V_{\lambda} = 0$ in projektorska endospletična regularne upodobitve na $V_{\lambda}$ je oblike $\Fcal(v)$ za nek $v \in V_{\lambda}$ z lastnostjo $v = v * v$, kar implicira $v = 0$ in s tem $V_{\lambda} = 0$, protislovje. Torej je $\widehat{\youngsym}(\rho_{\fun}) \cdot V_{\lambda} \neq 0$ in zato $V_{\lambda} \not\cong V_{\mu}$.

</div>

Preostane nam še dokaz leme.

<div class="dokaz">

(dokaz leme)

1.  Za vsaka $p \in P$, $q \in Q$ je $\sgn \cdot 1_q * \youngsym * 1_p = \youngsym$. Dokažimo najprej, da je Youngov simetrizator do skalarja natančno *edina* funkcija s to lastnostjo.

    Res, naj funkcija $f \in \hom(S_n, \CC)$ zadošča $\sgn \cdot 1_q * f * 1_p = f$. To pomeni, da za vsak $g \in G$ velja
    ```{math}
    f(g) = \sum_{x \in S_n \colon q x p = g} \sgn(q) \cdot f(g) = \sgn(q) \cdot f(q^{-1} g p^{-1}),
    ```
    kar lahko prepišemo v $f(qgp) = \sgn(q) \cdot f(g)$. Od tod sledi $f(qp) = \sgn(q) \cdot f(1)$. Na množici $QP$ se torej do skalarja $f(1)$ natančno funkcija $f$ ujema z Youngovim simetrizatorjem $\youngsym$.

    Preverimo še, da je izven množice $QP$ funkcija $f$ ničelna. V ta namen se spomnimo, da $P$ in $Q$ izhajata iz Youngove tabele $T$. Elementi $S_n$ naravno delujejo s permutacijami na množici tabel. Za $g \in S_n$ naj bo $g \cdot T$ rezultat tega delovanja z elementom $g$.

    <div class="domacanaloga">

    Za vsak $g \in S_n \backslash QP$ obstajata števili, ki sta zapisani v istem stolpcu $T$ in isti vrstici $g \cdot T$.

    </div>

    Naj bo $t$ transpozicija, ki zamenja števili iz predhodne naloge. Zanjo torej velja $t \in Q$ in $g^{-1} t g \in P$. S tem je
    ```{math}
    f(g) = f(t \cdot g \cdot g^{-1} t g) = \sgn(t) \cdot f(g) = - f(g),
    ```
    zato je $f(g) = 0$.

    Dokazano uporabimo z elementom $\youngsym * f * \youngsym$, kjer je $f$ poljubna funkcija. Vrednost $\sgn \cdot 1_q * (\youngsym * f * \youngsym) * 1_p$ izračunamo kot
    ```{math}
    (\sgn \cdot 1_q * \sgn \cdot 1_Q * 1_P) * f * (\sgn \cdot 1_Q * 1_P * 1_p) =
            \youngsym * f * \youngsym,
    ```
    od koder sledi želeno
    ```{math}
    \widehat{\youngsym}(\rho_{\fun}) \cdot (\youngsym * f) = \youngsym * f * \youngsym \in \CC \cdot \youngsym.
    ```

2.  Trdimo, da za vsako funkcijo $f \in \fun(S_n, \CC)$ velja enakost
    ```{math}
    1_{P_\mu} * f * (\sgn \cdot 1_{Q_{\lambda}}) = 0.
    ```
    Ker je ta enakost linearna v $f$, lahko predpostavimo, da je $f = 1_g$ za nek $g \in G$.

    Naj bosta $T_{\lambda}$, $T_{\mu}$ Youngovi tabeli razčlenitev $\lambda$, $\mu$, s katerima smo dobili grupi $P$ in $Q$. Tabelo $T_{\lambda}$ zamenjajmo s tabelo $g^{-1} \cdot T_{\lambda}$; ob tem se $Q_{\lambda}$ zamenja s $g^{-1} Q_{\lambda} g$. Z novimi tabelami je
    ```{math}
    1_{P_\mu} * (\sgn \cdot 1_{g^{-1} Q_{\lambda} g}) = 1_{P_\mu} * 1_{g^{-1}} * (\sgn \cdot 1_{Q_{\lambda}}) * 1_g.
    ```
    Če uspemo dokazati, da je leva stran ničelna, bo taka tudi desna, od koder po dodatni konvoluciji z $1_{g^{-1}}$ z desne sledi želena enakost.

    Predpostavimo torej lahko, da je $g = 1$. Kot v dokazu prejšnje točke najdemo transpozicijo $t \in Q_{\lambda} \cap P_{\mu}$. Z njo velja
    ```{math}
    1_{P_{\mu}} * (\sgn \cdot 1_{Q_{\lambda}}) = 
            \left( 1_{P_{\mu}} * 1_t \right) * \left( 1_{t^{-1}} * (\sgn \cdot 1_{Q_{\lambda}}) \right).
    ```
    Ker je $1_{P_{\mu}} * 1_t = 1_{P_{\mu}}$ in $1_{t^{-1}} * (\sgn \cdot 1_{Q_{\lambda}}) = - (\sgn \cdot 1_{Q_{\lambda}})$, je zadnja konvolucija enaka svoji negativni vrednosti, torej je ničelna.

</div>

Tekom dokaza izreka smo premislili, da je $\youngsym * \youngsym = n_{\lambda} \cdot \youngsym$ za nek skalar $n_{\lambda} \in \CC$. Linearna preslikava $\Fcal(\youngsym)$ slika v vektorski podprostor $V_{\lambda}$, na tem podprostoru pa deluje kot
```{math}
\Fcal(\youngsym) \cdot (\youngsym * f) 
    = \youngsym * \youngsym * f
    = n_{\lambda} \cdot (\youngsym * f),
```
torej kot skalarno množenje z $n_{\lambda}$. Ta skalar lahko izračunamo iz sledi preslikave $\Fcal(\youngsym)$. V standardni bazi iz karakterističnih funkcij namreč velja
```{math}
\Fcal(\youngsym) \cdot 1_g
    = \youngsym * 1_g
    = \left( x \mapsto \youngsym(x g^{-1}) \right)
    = \sum_{x \in S_n} \youngsym(x g^{-1}) \cdot 1_x
```
za vsak $g \in S_n$, torej so diagonalni členi prirejene matrike $\Fcal(\youngsym)$ enaki $\youngsym(1) = 1$. Od tod izračunamo sled preslikave $\Fcal(\youngsym)$ kot
```{math}
n_{\lambda} \cdot \dim V_{\lambda} 
    = \tr \Fcal(\youngsym)
    = \sum_{g \in S_n} 1
    = n!,
```
zato v posebnem velja $n_{\lambda} = n! / \dim V_{\lambda}$. Skalar $n_{\lambda}$ je torej neničelno racionalno število.

V posebnem lahko tvorimo endospletično $\Fcal(\youngsym / n_{\lambda})$ regularne upodobitve, ki je *projektorska spletična*[^5] na prostor $V_{\lambda}$. V tej posebni situaciji dobimo torej eksplicitno projekcijo z regularne na nerazcepno upodobitev $V_{\lambda}$. V standardni bazi ima matrika preslikave $\Fcal(\youngsym/n_{\lambda})$ racionalne koeficiente. Ker njeni stolpci razpenjajo prostor $V_{\lambda}$, lahko torej izberemo ortogonalno[^6] bazo $B_{\lambda} = \{ b_1, b_2, \dots, b_r \}$ prostora $V_{\lambda}$, v kateri ima vsak vektor $b_i$ racionalne koeficiente v standardni bazi. Ker grupa $S_n$ regularno deluje s permutacijami na standardni bazi, imajo torej tudi slike $\rho_{\fun}(g) \cdot b_i$ racionalne koeficiente v standardni bazi za vsak $g \in S_n$. Vsako od teh slik pa lahko razvijemo tudi po bazi $B_{\lambda}$ kot
```{math}
\rho_{\fun}(g) \cdot b_i
    = \sum_{b_j \in B_{\lambda}} \frac{\langle \rho_{\fun}(g) \cdot b_i, b_j \rangle}{\langle b_j, b_j \rangle} b_j,
```
in pri tem so koeficienti razvoja racionalni. V bazi $B_{\lambda}$ ima torej vsaka matrika $\rho_{\fun}(g)$ za $g \in S_n$ racionalne koeficiente. Upodobitev $\rho_{\lambda}$ je torej definirana nad poljem $\QQ$.

<div class="domacanaloga">

Naj bo $G$ končna grupa z upodobitvijo nad $\QQ$. Dokaži, da obstaja baza vektorskega prostora, v kateri je dana upodobitev definirana nad $\ZZ$. Nasvet: izberi neko bazo prostora in vsak njen element povpreči po grupi $G$.

</div>

<div class="posledica">

Vsaka nerazcepna upodobitev simetrične grupe je definirana nad $\ZZ$.

</div>

Vsak Spechtov modul $V_{\lambda}$ lahko z redukcijo po modulu $p$ za poljubno praštevilo $p$ reduciramo do vektorskega prostora nad končnim poljem $\FF_p$. Na ta način dobimo modularno upodobitev $\rho_{\lambda,p}$ simetrične grupe. Kot smo videli že v primeru $p = 3$, te upodobitve niso nujno nerazcepne. Izkaže se, da pa ima taka modularna upodobitev *enoličen nerazcepen kvocient* $D_{\lambda}$, če za razčlenitev $\lambda = 1^{i_1} 2^{i_2} \cdots n^{i_n}$ velja $i_j < p$ za vsak $j$. Takim ugodnim razčlenitvam pravimo <span class="definicija">$p$-regularne razčlenitve</span>. Izkaže se, da je število $p$-regularnih razčlenitev ravno enako številu konjugiranostnih razredov elementov v $S_n$, katerih red je *tuj* $p$. Na ta način dobimo vse modularne upodobitve simetrične grupe, a tega ne bomo dokazali (glej [(Curtis-Reiner 1962)](https://www.ams.org/books/chel/356/) in krajši povzetek [tukaj](https://math.berkeley.edu/~ltomczak/notes/Mich2022/RepSn_Notes.pdf)).

<div class="izrek">

Vsaka nerazcepna upodobitev $S_n$ nad $\FF_p$ je izomorfna $D_{\lambda}$ za neko $p$-regularno razčlenitev $\lambda$ števila $n$. Pri tem za različni razčlenitvi $\lambda , \mu$ velja $D_{\lambda} \not\cong D_{\mu}$.

</div>

<div class="zgled">

Opazujmo grupo $S_3$. Njene nerazcepne upodobitve nad $\CC$ dobimo iz razčlenitev $3^1$, $2^1 1^1$ in $1^3$, in sicer zaporedoma $\oneone$, $\rho$ in $\sgn$. Opazujmo praštevilo $p = 3$. Prvi dve od teh razčlenitev sta $3$-regularni, tretja pa ni. Iz prve dobimo nerazcepno upodobitev $\oneone$ nad $\FF_3$, druga upodobitev $\rho$ pa, kot smo videli, ni nerazcepna nad $\FF_3$, temveč ima podupodobitev $\oneone$ s kvocientom $\rho / \oneone \cong \sgn$. Dobimo torej dve nerazcepni upodobitvi nad $\FF_3$, in sicer $\oneone$ in $\sgn$. Nekoliko nenavadno je, da smo predznačno upodobitev nad $\FF_3$ pri tem dobili iz standardne upodobitve $S_3$ in *ne* iz predznačne upodobitve.

</div>

Modularni svet je mnogo bolj mističen od kompleksnega. Sodobna teorija upodobitev se povečini ukvarja s tem, kako *regularna* je kategorija upodobitev v odvisnosti od praštevila $p$.[^7] V zvezi s tem obstaja mnogo odprtih problemov.

<div class="odprtproblem">

Naj bo $p \leq n$ in naj bo $\lambda$ $p$-regularna razčlenitev $n$. Izračunaj večkratnosti $\mult_{\rho_{\lambda,p}}(\pi)$ nerazcepnih upodobitev $\pi$ nad $\FF_p$.

</div>

Ta problem je razrešen le za razčlenitve $\lambda$ z največ dvema deloma, torej s $k \leq 2$. Za $k = 3$ sodobna bilijardna domneva [(Lusztig-Williamson 2018)](https://arxiv.org/pdf/1703.05898.pdf) predvideva, da se te večkratnosti obnašajo po zakonu nekega zakompliciranega [dinamičnega sistema](https://www.youtube.com/watch?v=Ru0Zys1Vvq4).

### Vrednosti karakterjev

Premislili smo že, da so vsi Spechtovi moduli definirani nad $\ZZ$, zato so vrednosti karakterjev simetrične grupe vselej cela števila. Poznamo pa celo dokaj preprost način, kako lahko eksplicitno določimo vse vrednosti karakterjev nerazcepnih upodobitev. Izrekli ga bomo v jeziku polinomskega kolobarja $\CC[\mathbf{x}] = \CC[x_1, x_2, \dots, x_k]$. Potrebovali bomo nekaj posebnih polinomov iz tega kolobarja, in sicer <span class="definicija">diskriminanto</span>
```{math}
\Delta(\mathbf{x}) = \prod_{1 \leq i < j \leq k} (x_i - x_j)
```
ter <span class="definicija">potenčne vsote</span>
```{math}
P_j(\mathbf{x}) = x_1^j + x_2^j + \cdots + x_k^j
```
za $j \in \NN$. Za dan polinom $P(\mathbf{x}) \in \CC[\mathbf{x}]$ označimo s
```{math}
[P(\mathbf{x})]_{(\ell_1, \ell_2, \dots, \ell_k)}
```
njegov koeficient pred monomom $x_1^{\ell_1} x_2^{\ell_2} \cdots x_k^{\ell_k}$.

<div class="izrek">

Naj bo $\lambda = (\lambda_1, \lambda_2, \dots, \lambda_k)$ razčlenitev $n$ in $\chi_{\lambda}$ pripadajoči karakter. Naj bo $\conclass_{1^{i_1} 2^{i_2} \cdots n^{i_n}}$ konjugiranostni razred. Tedaj je
```{math}
\chi_{\lambda}\left(\conclass_{1^{i_1} 2^{i_2} \cdots n^{i_n}}\right) =
    \left[ \Delta(\mathbf{x}) \cdot P_1(\mathbf{x})^{i_1} P_2(\mathbf{x})^{i_2} \cdots P_n(\mathbf{x})^{i_n} \right]_{(\ell_1, \ell_2, \dots, \ell_k)},
```
kjer je
```{math}
\ell_1 = \lambda_1 + k - 1, \quad
    \ell_2 = \lambda_2 + k - 2, \quad
    \dots, \quad
    \ell_k = \lambda_k.
```

</div>

Dokaz temelji na poznavanju osnov teorije simetričnih funkcij, ki jih ponavadi spoznamo pri kombinatoričnih predmetih, zato ga brez prehude žalosti izpustimo. Poglejmo pa si nekaj primerov uporabe izreka.

<div class="zgled">

- Naj bo $n = 7$ in $\lambda = (4,3)$. Izračunajmo vrednost karakterja v permutaciji $(1 \ 2)(3 \ 4)$. Velja $i_1 = 3$, $i_2 = 2$, $\ell_1 = 5$, $\ell_2 = 3$ in s tem
  ```{math}
  \chi_{(4,3)}(\conclass_{1^3 2^2}) = 
      \left[ (x_1 - x_2) \cdot (x_1 + x_2)^3 (x_1^2 + x_2^2)^2 \right]_{(5,3)} =
      2.
  ```

- Izračunajmo vrednost poljubnega karakterja $\chi_{\lambda}$ v dolgem ciklu $(1 \ 2 \ \cdots \ n) \in S_n$. Konjugiranostni razred je torej $\conclass_{n^1}$ in izračunati moramo koeficient
  ```{math}
  \left[ \Delta(\mathbf{x}) \cdot (x_1^n + x_2^n + \cdots + x_k^n) \right]_{(\ell_1, \ell_2, \dots, \ell_k)}.
  ```
  Diskriminanta $\Delta(\mathbf{x})$ je enaka Vandermondovi determinanti
  ```{math}
  \Delta(\mathbf{x}) = \sum_{\sigma \in S_k} \sgn(\sigma) \cdot x_1^{\sigma(k) - 1} x_2^{\sigma(k-1) - 1} \cdots x_k^{\sigma(1) - 1}.
  ```
  Opazujmo potence spremenljivke $x_1$. Opazimo, da velja $\ell_1 = \lambda_1 + k - 1 \geq k$, zato iščemo monome, katerih potenca pri $x_1$ je vsaj $k$. Edina možnost je, da ta monom izhaja iz produkta diskriminante in člena $x_1^n$. Iščemo torej člen
  ```{math}
  \left[ \sum_{\sigma \in S_k} \sgn(\sigma) \cdot x_1^{\sigma(k) - 1 + n} x_2^{\sigma(k-1) - 1} \cdots x_k^{\sigma(1) - 1} \right]_{(\ell_1, \ell_2, \dots, \ell_k)}.
  ```
  Oglejmo si zdaj spremenljivko $x_2$. Da bo obstajal kak relevanten monom, mora veljati $\ell_2 = \sigma(k-1) - 1$. Ker je $\sigma(k-1) \leq k$, sledi $\ell_2 \leq k -1$ in od tod $\lambda_2 \leq 1$. Edina možnost, da je $\chi_{\lambda}(\conclass_{n^1}) \neq 0$, je torej, da ima razčlenitev $\lambda$ vse člene od drugega dalje enake $1$ in je zato oblike
  ```{math}
  \lambda = (n-s, 1, 1, \dots, 1)
  ```
  za nek $0 \leq s \leq n-1$. Takšni razčlenitvi pravimo <span class="definicija">kljuka</span>.

  <figure>
  <img src="img/img_kljuka.png" style="width:33.0%" />
  <figcaption>Kljuka <span class="math inline"><em>λ</em> = (7, 1, 1)</span>.</figcaption>
  </figure>

  Za kljuko je $k = s+1$ in $(\ell_1, \ell_2, \dots, \ell_k) = (n, k-1, k-2, \dots, 1)$, od koder ni težko izračunati, da edini relevanten monom izhaja iz permutacije $\sigma = (1 \ 2 \ \cdots \ k)$, zato je nazadnje
  ```{math}
  \chi_{\lambda}(C_{n^1}) = \sgn(\sigma) = (-1)^s.
  ```
  Vrednost karakterja v dolgem ciklu je torej neničelna le za kljuke, v katerih pa ima vrednost $\pm 1$.

</div>

<div class="domacanaloga">

Izračunaj vrednost poljubnega karakterja $\chi_{\lambda}$ v konjugiranostnem razredu transpozicij.

</div>

S Frobeniusovo formulo lahko določimo stopnje nerazcepnih upodobitev simetrične grupe. Za to bomo potrebovali koncept kljuke, ki je malo splošnejši od tiste, ki smo jo videli v zadnjem zgledu. Opazujmo Youngov diagram razčlenitve $\lambda$. Za vsako celico $(i,j)$ diagrama, kjer $i$ predstavlja vrstico in $j$ stopec, je <span class="definicija">kljuka</span> $H_{\lambda}(i,j)$ množica tistih celic, ki so desno ali pod celico $(i,j)$, vključivši celico $(i,j)$.[^8] <span class="definicija">Dolžina kljuke</span> $H_{\lambda}(i,j)$ je enaka številu celic v kljuki, se pravi $|H_{\lambda}(i,j)|$.

<figure>
<img src="img/img_dolzine_kljuk.png" style="width:33.0%" />
<figcaption>V celicah Youngovega diagrama razčlenitve <span class="math inline"><em>λ</em> = (5, 3, 1)</span> so zapisane dolžine kljuk. Označena je kljuka <span class="math inline"><em>H</em><sub><em>λ</em></sub>(1, 3)</span>.</figcaption>
</figure>

<div class="posledica">

Naj bo $\lambda$ razčlenitev $n$. Tedaj je
```{math}
\dim V_{\lambda} = \frac{n!}{\prod_{i,j} |H_{\lambda}(i,j)|}.
```

</div>

<div class="dokaz">

Velja
```{math}
\dim V_{\lambda} = \chi_{\lambda}(\conclass_{1^n}) =
    \left[ \Delta(\mathbf{x}) \cdot (x_1 + x_2 + \cdots + x_k)^n \right]_{(\ell_1, \ell_2, \dots, \ell_k)}.
```
Diskriminanto razvijemo kot v zadnjem zgledu, drugi člen pa po multinomski formuli kot
```{math}
(x_1 + x_2 + \cdots + x_k)^n = \sum_{j_1 + j_2 + \cdots + j_k = n} \frac{n!}{j_1! j_2! \cdots j_k!} x_1^{j_1} x_2^{j_2} \cdots x_k^{j_k}.
```
Ko razviti vsoti zmnožimo, dobimo člen $x_1^{\ell_1} x_2^{\ell_2} \cdots x_k^{\ell_k}$, če in samo če za neko permutacijo $\sigma \in S_n$ in nabor $j_1, j_2, \dots, j_k$ velja $\sigma(k - i + 1) - 1 + j_i = \ell_i$. Iskani koeficient je torej enak
```{math}
\sum_{\sigma} \sgn(\sigma) \cdot \frac{n!}{(\ell_1 - \sigma(k) + 1)! (\ell_2 - \sigma(k-1) + 1)! \cdots (\ell_k - \sigma(1) + 1)!},
```
kjer seštevamo po tistih $\sigma \in S_k$, za katere velja $\ell_i - \sigma(k-i+1) + 1 \geq 0$ za vsak $i$. To vsoto lahko prepišemo v
```{math}
\frac{n!}{\ell_1! \ell_2! \cdots \ell_k!} \cdot \sum_{\sigma} \sgn(\sigma) \cdot \prod_{j = 1}^k \ell_j (\ell_j - 1) \cdots (\ell_j - \sigma(k-j+1) + 2).
```
Zadnjo vsoto lahko seštevamo po vseh $\sigma \in S_k$, saj so členi, v katerih je $\ell_i - \sigma(k-i+1) + 1 < 0$, ničelni. To vsoto zato prepoznamo kot determinanto matrike razsežnosti $k \times k$ z $j$-tim stolpcem
```{math}
1, \ \ell_j, \ \ell_j(\ell_j - 1), \ \dots, \ell_j(\ell_j - 1) \cdots (\ell_j - k + 2).
```
Ta determinanta je enaka Vandermondovi determinanti, zato je iskani koeficient enak
```{math}
\frac{n!}{\ell_1! \ell_2! \cdots \ell_k!} \cdot \prod_{1 \leq i < j \leq n} (\ell_i - \ell_j).
```
Če ima $\lambda$ en sam stolpec in je torej $\lambda = (1,1,\dots,1)$, potem je $k = n$ in $\ell_i = n - i + 1$, zato je zadnje število enako
```{math}
\frac{n!}{n! (n-1)! \cdots 1!} \cdot \prod_{1 \leq i < j \leq n} (j-i) =
    \frac{n!}{n! (n-1)! \cdots 1!} \cdot \prod_{1 < j \leq n} (j-1)! =
    1,
```
kot mora biti, saj že vemo, da je v tem primeru $V_{\lambda} \cong \sgn$. Dolžine kljuk so $|H_{\lambda}(i,1)| = n - i + 1$, zato formula o kljukah za ta trivialen primer drži. Splošnega primera ni težko izpeljati z indukcijo (glej nalogo spodaj). S tem je formula o kljukah dokazana.

</div>

<div class="domacanaloga">

Z indukcijo na število stolpcev Youngovega diagrama $\lambda$ dokaži, da je
```{math}
\frac{n!}{\ell_1! \ell_2! \cdots \ell_k!} \cdot \prod_{i < j} (\ell_i - \ell_j) = \frac{n!}{\prod_{i,j}|H_{\lambda}(i,j)|}.
```

</div>

<div class="zgled">

Iz formule o dolžinah kljuk takoj izračunamo stopnjo standardne upodobitve. Usteza ji razčlenitev $(n-1,1)$, torej je njena stopnja enaka
```{math}
\frac{n!}{1 \cdot 2 \cdot \cdots \cdot (n-2) \cdot n \cdot 1} = n-1.
```

</div>

V zvezi s tabelo karakterjev simetrične grupe omenimo še sodobnejši presenetljiv rezultat [(Miller 2014)](https://link.springer.com/article/10.1007/s00209-014-1290-x), v katerem avtor dokaže, da so vrednosti skoraj vseh karakterjev v skoraj vseh grupnih elementih ničelne. Natančneje, če enakomerno naključno izberemo $g \in S_n$ in $\pi \in \Irr(S_n)$, potem je
```{math}
\lim_{n \to \infty} \PP_{g, \pi}\left(\chi_{\pi}(g) = 0\right) = 1.
```
Avtor omeni analogno vprašanje glede same tabele karakterjev.

<div class="odprtproblem">

Enakomerno naključno izberimo konjugiranostni razred $\conclass$ v $S_n$ in $\pi \in \Irr(S_n)$. Kaj lahko povemo o obnašanju zaporedja $\PP_{\conclass, \pi}\left( \chi_{\pi}(\conclass) = 0 \right)$, ko gre $n$ čez vse meje?

</div>

Na podlagi ekstenzivnih Monte Carlo simulacij [(Miller-Scheinerman 2025)](https://www.ams.org/journals/mcom/2025-94-351/S0025-5718-2024-03964-9/) ponujata nekaj domnev v tej smeri.

### Alternirajoče grupe

Oglejmo si, kako lahko iz tabele karakterjev simetrične grupe skoraj popolnoma določimo tabelo karakterjev alternirajoče grupe $A_n$.

Določimo najprej konjugiranostne razrede. Naj bo $\conclass = \sigma^{A_n} \subseteq A_n$ konjugiranostni razred. Ta množica je torej zaprta za konjugiranje z vsemi sodimi permutacijami. Če velja tudi $\sigma^{(1 \ 2)} \in \conclass$, potem je $\conclass$ celo konjugiranostni razred v $S_n$ in torej ustreza neki razčlenitvi števila $n$. Prav lahko pa se zgodi, da $\conclass$ ni zaprt za konjugiranje z $(1 \ 2)$. V tem primeru je množica $\conclass \cup \conclass^{(1 \ 2)}$ konjugiranostni razred permutacije $\sigma$ v $S_n$ in zato ustreza neki razčlenitvi števila $n$. Konjugiranostne razrede grupe $A_n$ dobimo torej iz konjugiranostnih razredov sodih permutacij v $S_n$, in sicer določeni razredi v $S_n$ ostanejo konjugiranostni razredi v $A_n$, drugi pa se razcepijo na dva konjugiranostna razreda v $A_n$ enake velikosti. Ni težko prepoznati, kateri razredi se razcepijo.

<div class="domacanaloga">

Naj bo $\conclass$ konjugiranostni razred sode permutacije v $S_n$, ki ustreza razčlenitvi $\lambda = (\lambda_1, \lambda_2, \dots, \lambda_k)$. Dokaži, da se $\conclass$ razcepi v dva konjugiranostna razreda v $A_n$, če in samo če so vsi $\lambda_i$ lihi in različni med sabo.

</div>

Poskusimo zdaj na podoben način razumeti še nerazcepne upodobitve grupe $A_n$. Naj bo $\lambda$ razčlenitev $n$, ki ji pritiče nerazcepna upodobitev $\rho_{\lambda}$ na prostoru $V_{\lambda}$ s karakterjem $\chi_{\lambda}$. Opazujmo zožitev karakterja $\chi_{\lambda}|_{A_n}$ na $A_n$. Po ortonormiranosti karakterjev v $S_n$ velja
```{math}
\langle \chi_{\lambda}|_{A_n}, \chi_{\lambda}|_{A_n} \rangle
    +
    \frac{1}{|A_n|} \sum_{\sigma \in S_n \backslash A_n} |\chi_{\lambda}(\sigma)|^2
    =
    \frac{1}{|A_n|} \cdot |S_n| \langle \chi_{\lambda}, \chi_{\lambda} \rangle
    = 2.
```
Torej je $\langle \chi_{\lambda}|_{A_n}, \chi_{\lambda}|_{A_n} \rangle \in \{ 1, 2 \}$, zato je $\rho_{\lambda}|_{A_n}$ bodisi nerazcepna upodobitev bodisi vsota dveh neizomorfnih nerazcepnih upodobitev. Drugi primer nastopi, če in samo če je $\chi_{\lambda}|_{S_n \backslash A_n} = 0$, kar je ekvivalentno izomorfizmu $\rho_{\lambda} \cong \sgn \otimes \rho_{\lambda}$. Zadnja upodobitev je izomorfna $\rho_{\lambda^\prime}$, zato se upodobitev $\rho_{\lambda}$ razcepi na $A_n$, če in samo če je $\lambda = \lambda^\prime$, se pravi da je $\lambda$ simetrična razčlenitev. V tem primeru lahko zapišemo $\chi_{\lambda}|_{A_n} = \alpha + \beta$, kjer sta $\alpha, \beta$ nerazcepna karakterja $A_n$. Ni se težko prepričati, da zanju velja $\beta(\sigma) = \alpha(\sigma^{(1 \ 2)})$ za vsak $\sigma \in A_n$, torej sta v posebnem upodobitvi, na katere razpade $\rho_{\lambda}$, enake razsežnosti. Konkretne vrednosti karakterjev $\alpha$ in $\beta$ lahko izračunamo s pomočjo ortogonalnosti karakterjev.

S štetjem konjugiranostnih razredov v $A_n$ se ni težko prepričati, da na opisan način dobimo vse nerazcepne upodobitve alternirajoče grupe. Podrobnosti so podrobno prikazane v (Fulton-Harris 2004).

## Splošne linearne grupe

Opazujmo <span class="definicija">splošno linearno grupo</span>
```{math}
G_p = {\textstyle \GL_2(\FF_p)} =
    \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \mid a,b,c,d \in \FF_p, \ ad - bc \neq 0 \right\}
```
obrnljivih matrik razsežnosti $2 \times 2$ nad končnim poljem $\FF_p$, kjer je $p$ praštevilo. Njeno kategorijo upodobitev bomo obravnavali nad $\CC$. Še pred tem pa moramo bolje spoznati to grupo.[^9]

### Osnovne poteze

Grupo $G_p$ lahko razumemo s pomočjo njenih podgrup
```{math}
\begin{aligned}
    B_p &= \left\{ \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} \mid a,d \in \FF_p^*, \ b \in \FF_p \right\}, \\
    D_p &= \left\{ \begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix} \mid a,d \in \FF_p^* \right\}, \\
    U_p &= \left\{ \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} \mid b \in \FF_p \right\}.
\end{aligned}
```
Grupa $B_p$ je <span class="definicija">Borelova podgrupa</span>, grupa $U_p$ pa <span class="definicija">unipotentna podgrupa</span>. Seveda je $B_p/U_p = D_p$. Grupa $G_p$ ima torej vrsto podgrup
```{math}
G_p \geq B_p \geq U_p \geq 1.
```
Borelova podgrupa *ni* edinka v $G_p$, ima pa kvocientna množica $G_p/B_p$ odsekov vsekakor pomembno vlogo. Grupa $G_p$ namreč deluje na ravnini $\FF_p^2$ z matričnim množenjem in za tem na množici premic v tej ravnini, se pravi
```{math}
\PP^1(\FF_p) = \{ \ell \leq \FF_p^2 \mid \dim \ell = 1 \},
```
čemur pravimo <span class="definicija">projektivna premica</span> nad $\FF_p$. Grupa $G_p$ deluje na tej premici tranzitivno in stabilizator premice $e_1$ je ravno Borelova podgrupa $B_p$. Projektivno premico lahko zato enačimo z množico $G_p/B_p$. V posebnem tako dobimo homomorfizem
```{math}
\Pi \colon G_p \to \Sym(\PP^1(\FF_p)) = S_{p+1},
```
o katerem bomo več povedali nekoliko kasneje. Za zdaj ne spreglejmo, da od tod takoj izračunamo $|G_p/B_p| = p+1$ in s tem
```{math}
|G_p| = |G_p/B_p| \cdot |B_p| = (p+1) \cdot (p-1)^2 p.
```

Grupa $G_p$ je opremljena tudi z determinantnim homomorfizmom
```{math}
\det \colon G_p \to \FF_p^*.
```
Jedro tega homomorfizma je <span class="definicija">specialna linearna grupa</span>
```{math}
{\textstyle \SL_2(\FF_p)} = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \mid a,b,c,d \in \FF_p, \ ad - bc = 1 \right\}.
```
Velja $|\SL_2(\FF_p)| = |G_p|/(p-1) = (p+1)p(p-1)$. Izpostavimo dva posebna elementa te grupe,
```{math}
S_+ = \begin{pmatrix}
        1 & 1 \\ 0 & 1
    \end{pmatrix}, \quad
    S_- = \begin{pmatrix}
        1 & 0 \\ 1 & 1
    \end{pmatrix}.
```
Levo množenje s tema dvema elementoma ustreza izvajanju vrstičnih operacij na dani matriki,
```{math}
S_+ \cdot 
    \begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix}
    = 
    \begin{pmatrix}
        a+c & b+d \\ c & d
    \end{pmatrix}, \quad
    S_- \cdot 
    \begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix}
    = 
    \begin{pmatrix}
        a & b \\ c+a & d+b
    \end{pmatrix}
```
Ker lahko vsako matriko v $\SL_2(\FF_p)$ z vrstičnimi operacijami pripeljemo do identitete, sklenemo, da elementa $S_+$, $S_-$ *generirata* grupo $\SL_2(\FF_p)$.

<div class="zgled">

Naj bo $p = 2$. Grupa $G_2$ v tem primeru enaka $\SL_2(\FF_2)$ in je moči $6$. Naravno deluje z matričnim množenjem na množici treh neničelnih vektorjev $\FF_2^2 \backslash \{ 0 \} = \{ e_1, e_2, e_1 + e_2 \}$. Na ta način dobimo homomorfizem
```{math}
G_2 \to S_3, \quad
        S_+ \mapsto (2 \ 3), \ 
        S_- \mapsto (1 \ 3).
```
ki je surjektiven, ker zapisani transpoziciji generirata grupo $S_3$. Ker imata obe grupi enako moč, je celo izomorfizem, torej je $G_2 \cong S_3$.

</div>

<div class="trditev">

Za $p > 2$ je $[G_p, G_p] = \SL_2(\FF_p)$.

</div>

<div class="dokaz">

Ker je $G_p/\SL_2(\FF_p)$ komutativna, je $[G_p,G_p] \leq \SL_2(\FF_p)$. Za obratno neenakost upoštevamo račun
```{math}
\left[ 
        S_+^{-2^{-1}}, 
        \begin{pmatrix}
            1 & 0 \\ 0 & -1 
        \end{pmatrix}
    \right] =
    S_+^{2^{-1}} \cdot 
    \begin{pmatrix}
        1 & 0 \\ 0 & -1 
    \end{pmatrix}
    \cdot S_+^{-2^{-1}} \cdot
    \begin{pmatrix}
        1 & 0 \\ 0 & -1 
    \end{pmatrix}
    = S_+
```
in sklenemo $S_+ \in [G_p, G_p]$. Sorodno dobimo $S_- \in [G_p, G_p]$. Ker $S_+,S_-$ generirata $\SL_2(\FF_p)$, dobimo še drugo vsebovanost.

</div>

Nazadnje upoštevajmo oba posebna homomorfizma, $\Pi$ in $\det$. Presek njunih jeder sestoji iz skalarnih matrik z determinanto $1$, torej je enak $\{ I, -I \}$. Ta podgrupa je edinka v $\SL_2(\FF_p)$, zato lahko tvorimo kvocient
```{math}
{\textstyle \PSL_2(\FF_p)} = \frac{\SL_2(\FF_p)}{\{ I, -I \}}.
```

<div class="zgled">

Za $p = 2$ je $\PSL_2(\FF_2) = \SL_2(\FF_2) \cong S_3$. Za $p = 3$ se grupa $\PSL_2(\FF_3)$ prek delovanja $\Pi$ vloži v simetrično grupo $S_4$. Ker je $|\PSL_2(\FF_3)| = 12$, je slika te vložitve podgrupa indeksa $2$ v $S_4$, kar pomeni, da gre za alternirajočo podgrupo. Sledi $\PSL_2(\FF_3) \cong A_4$.

</div>

<div class="domacanaloga">

Naj bo $p = 5$. Grupa $\PSL_2(\FF_5)$ je moči $60$. Poišči njene $2$-podgrupe Sylowa. Na množici teh podgrup grupa $\PSL_2(\FF_5)$ deluje tranzitivno. Iz tega delovanja izpelji, da je $\PSL_2(\FF_5) \cong A_5$.

</div>

<div class="izrek">

Za $p > 3$ je grupa $\PSL_2(\FF_p)$ enostavna.

</div>

<div class="dokaz">

Izrek je prvi izrekel Galois leta 1831, ni pa podal dokaza. Prvi objavljen dokaz najdemo v [(Jordan 1870)](https://archive.org/details/traitdessubsti00jorduoft/page/n15/mode/2up). Nekoliko bolj sodobna različica dokaza je v [Conradovih zapiskih](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf).

</div>

Družina grup $G_p$ za praštevila $p$ je torej dobra prijateljica ene od fundamentalnih družin končnih enostavnih grup.

### Konjugiranostni razredi

Predpostavimo, da je $p > 2$. Konjugiranostni razredi v $G_p$ so enaki podobnostnim razredom matrik. Te najlažje sistematično obravnavamo prek lastnosti njihovih karakterističnih polinomov, ki so stopnje $2$. Bodisi je ta polinom razcepen (z eno dvojno ničlo ali dvema različnima v $\FF_p$) bodisi je nerazcepen. V primeru dvojnih ničel obravnavamo še možnost, da matrika morda ni diagonalizabilna. Na ta način dobimo naslednje konjugiranostne razrede.

1.  <span class="definicija">Skalarji</span>. Naj ima element $g \in G_p$ karakteristični polinom z dvojno ničlo $a \in \FF_p^*$ in je hkrati diagonalizabilen. Tedaj je $g$ skalarna matrika
    ```{math}
    \begin{pmatrix}
                a & 0 \\ 0 & a
            \end{pmatrix}.
    ```
    Vsak tak element je centralen v $G_p$, zato je njegov konjugiranostni razred velikosti $1$. Vseh takih razredov je $p-1$.

2.  <span class="definicija">Nediagonalizabilni elementi</span>. Naj ima element $g \in G_p$ karakteristični polinom z dvojno ničlo $a \in \FF_p^*$ in hkrati *ni* diagonalizabilen. Tedaj je po Jordanovi formi $g$ podoben matriki
    ```{math}
    \begin{pmatrix}
                a & 1 \\ 0 & a
            \end{pmatrix}.
    ```
    Centralizator vsakega takega elementa je enak
    ```{math}
    C_p = \left\{ \begin{pmatrix}
          x & t \\ 0 & x
      \end{pmatrix} \mid x \in \FF_p^*, \ t \in \FF_p \right\} = S_p \times U_p,
    ```
    kjer je $S_p$ množica skalarnih matrik. Velja $|C_p| = (p-1)p$. Konjugiranostni razred je torej velikosti $p^2 - 1$. Vseh takih razredov je $p-1$.

3.  <span class="definicija">Razcepni polenostavni elementi</span>. Naj ima element $g \in G_p$ karakteristični polinom z dvema različnima ničlama $a,b \in \FF_p^*$. Tak element je diagonalizabilen in zato podoben
    ```{math}
    \begin{pmatrix}
                a & 0 \\ 0 & b
            \end{pmatrix}.
    ```
    Centralizator vsakega takega elementa je enak
    ```{math}
    T_r = D_p = \left\{ \begin{pmatrix}
                x & 0 \\ 0 & y
            \end{pmatrix} \mid x, y \in \FF_p^* \right\}.
    ```
    in je zato moči $(p-1)^2$. Konjugiranostni razred je torej velikosti $p(p+1)$. Vseh takih razredov je $\binom{p-1}{2} = (p-1)(p-2)/2$.

4.  <span class="definicija">Nerazcepni polenostavni elementi</span>. Naj ima element $g \in G_p$ *nerazcepen* karakteristični polinom. Ta polinom torej nima ničel v $\FF_p$, ima pa ničle v razširitvi $F$ tega polja z ničlama karakterističnega polinoma. Ker je $p > 2$, sta ti dve ničli različni.[^10] Razširitev $F/\FF_p$ je stopnje $2$, zato jo lahko predstavimo kot
    ```{math}
    F \cong \frac{\FF_p[X]}{(X^2 - \epsilon)} = \FF_p(\sqrt{\epsilon}),
    ```
    kjer $\epsilon \in \FF_p^*$ *ni* kvadrat v $\FF_p$. To polje je opremljeno z Galoisjevim avtomorfizmom $\sigma \colon \sqrt{\epsilon} \mapsto - \sqrt{\epsilon}$ reda $2$. Če je $\lambda$ lastna vrednost $g$, je torej tudi $\lambda^{\sigma}$ lastna vrednost in pripadajoča lastna vektorja sta $v$ in $v^{\sigma}$. Zamenjajmo bazo v $w_2 = v + v^{\sigma}$ in $w_1 = (v - v^{\sigma})/\sqrt{\epsilon}$. Ta dva vektorja sta invariantna za avtomorfizem $\sigma$, zato imata obe komponenti v $\FF_p$. V tej bazi ima element $g$ matriko
    ```{math}
    \begin{pmatrix}
                a & \epsilon b \\ b & a
            \end{pmatrix},
    ```
    kjer je $a = (\lambda + \lambda^{\sigma})/2 \in \FF_p$ in $b = (\lambda - \lambda^{\sigma})/(2 \sqrt{\epsilon}) \in \FF_p^*$. Centralizator vsakega takega elementa je enak
    ```{math}
    T_{nr} = \left\{ \begin{pmatrix}
                x & \epsilon y \\ y & x
            \end{pmatrix} \mid x, y \in \FF_p, \ (x,y) \neq (0,0) \right\}.
    ```
    Konjugiranostni razred je torej velikosti $p(p-1)$. Vseh takih razredov je $p (p-1)/2$.[^11]

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:--:|:--:|:--:|:--:|
| število razredov | $p-1$ | $p-1$ | $(p-1)(p-2)/2$ | $p(p-1)/2$ |
| velikost razreda | $1$ | $p^2 - 1$ | $p(p+1)$ | $p(p-1)$ |

Konjugiranostni razredi v $G_p$: njihov tip, število razredov določenega tipa in velikost razreda

Za velika praštevila $p$ velja $|G_p| \sim p^4$.[^12] Hkrati iz izračunov števila razredov in njihovih velikosti vidimo, da je število polenostavnih elementov asimptotsko primerljivo s $p^4$, razdeljeno približno na polovico med razcepnimi in nerazcepnimi elementi. Generični elementi v $G_p$ so za velika praštevila torej polenostavni.

Seštejemo število vseh konjugiranostnih razredov in dobimo
```{math}
\kk(G_p) = p^2 - 1.
```
Grupa $G_p$ ima torej $p^2-1$ nerazcepnih kompleksnih upodobitev.

Preden nadaljujemo z natančnim določanjem teh upodobitev, se še enkrat ozrimo na klasifikacijo konjugiranostnih razredov. Tekom določanja velikosti razredov smo naleteli na dva posebna centralizatorja polenostavnih elementov, in sicer $T_r$ in $T_{nr}$. Ta dva centralizatorja bosta igrala pomembno vlogo v teoriji upodobitev grupe $G_p$. Prvemu pravimo <span class="definicija">razcepni torus</span>, drugemu pa <span class="definicija">nerazcepni torus</span>. Za razcepni torus velja
```{math}
T_r \cong \FF_p^* \times \FF_p^*,
```
nerazcepni torus pa identificiramo kot[^13]
```{math}
T_{nr} \cong \FF_p(\sqrt{\epsilon})^*, \quad
    \begin{pmatrix}
        x & \epsilon y \\ y & x
    \end{pmatrix}
    \mapsto x + \sqrt{\epsilon} y.
```
Obe grupi, $\FF_p^*$ in $\FF_p(\sqrt{\epsilon})^*$, sta ciklični grupi. Prva je moči $p-1$, druga pa moči $p^2 - 1$.

### Tabela karakterjev, 1. del

Predpostavimo, da je $p > 2$. Določimo najprej enorazsežne upodobitve grupe $G_p$. Ker je $[G_p, G_p] = \SL_2(\FF_p) = \ker (\det)$, vse enorazsežne upodobitve dobimo tako, da najprej uporabimo determinanto $\det \colon G_p \to \FF_p^*$, za tem pa poljubno upodobitev abelove grupe $\FF_p^*$. Za vsak homomorfizem $\chi \colon \FF_p^* \to \CC^*$ dobimo torej enorazsežno upodobitev $\chi \circ \det$ grupe $G_p$ in vse enorazsežne upodobitve so take oblike. Vseh teh upodobitev je $|\FF_p^*| = p-1$.

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:--:|:--:|:--:|:--:|
| $\chi \circ \det$ | $\chi(a)^2$ | $\chi(a)^2$ | $\chi(a) \chi(b)$ | $\chi(a^2 - \epsilon b^2)$ |

Enorazsežni karakterji $G_p$

Nadaljujmo s pomočjo homomorfizma $\Pi \colon G_p \to S_{p+1}$, ki opisuje permutacijsko delovanje $G_p$ na projektivni premici. Od tod dobimo permutacijsko upodobitev $G_p$ na $\CC[\PP^1(\FF_p)]$. Kot smo videli že v primeru simetrične grupe, ta upodobitev *ni* nerazcepna, saj vedno vsebuje $\oneone$. Naj bo $\St$ komplement $\oneone$ v tej permutacijski upodobitvi. Ta komplement je do izomorfizma natako enolično določen in mu pravimo <span class="definicija">Steinbergova upodobitev</span>.[^14] Vrednosti karakterjev $\St$ ni težko izračunati. Račun pokaže $\langle \St, \St \rangle = 1$, zato je $\St$ nerazcepna upodobitev.

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:--:|:--:|:--:|:--:|
| $\St$ | $p$ | $0$ | $1$ | $-1$ |

Steinbergov karakter $G_p$

Steinbergovo upodobitev lahko tenzoriramo s poljubno enorazsežno in dobimo $\St \otimes (\chi \circ \det)$, kar označimo krajše kot $\St(\chi)$. Za $\chi = \oneone$ dobimo običajno Steinbergovo upodobitev. Vse te upodobitve so tudi nerazcepne.

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:--:|:--:|:--:|:--:|
| $\St(\chi)$ | $p \chi(a)^2$ | $0$ | $\chi(a) \chi(b)$ | $- \chi(a^2 - \epsilon b^2)$ |

Posplošeni Steinbergov karakter $G_p$

Do zdaj smo našteli $2(p-1)$ nerazcepnih upodobitev, iščemo pa jih $p^2 - 1$. Še veliko jih manjka! Sledeč filozofiji Artina in Brauerja nadaljne nerazcepne upodobitve iščemo z indukcijo iz podgrup $G_p$. Opazujmo Borelovo podgrupo $B_p$. Ta grupa je opremljena s projekcijo na razcepni torus
```{math}
B_p \to B_p / U_p = D_p = T_r = \FF_p^* \times \FF_p^*.
```
Nerazcepne upodobitve razcepnega torusa so ravno produkti $\chi_1 \times \chi_2$, kjer sta $\chi_1$, $\chi_2$ nerazcepni upodobitvi prvega oziroma drugega faktorja torusa. Na ta način dobimo nerazcepne upodobitve Borelove podgrupe,
```{math}
\rho(\chi_1, \chi_2) \colon B_p \to \CC^*, \quad
    \begin{pmatrix}
        a & b \\ 0 & d
    \end{pmatrix} \mapsto
    \chi_1(a) \chi_2(d).
```
Vsako od teh upodobitev induciramo na grupo $G_p$ in dobimo upodobitev
```{math}
\pi(\chi_1, \chi_2) = \textstyle \Ind^{G_p}_{B_p}(\rho(\chi_1, \chi_2))
```
razsežnosti $|G_p/B_p| = p+1$. Karakter take upodobitve lahko izračunamo s formulo za vrednosti karakterjev inducirane upodobitve.

<div class="domacanaloga">

Izračunaj vrednosti karakterjev upodobitve $\pi(\chi_1, \chi_2)$.

</div>

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:---|:---|:---|:---|
| $\pi(\chi_1, \chi_2)$ | $(p+1) \chi_1(a) \chi_2(a)$ | $\chi_1(a) \chi_2(a)$ | $\chi_1(a) \chi_2(b) + \chi_2(a) \chi_1(b)$ | $0$ |

Karakter upodobitve $\pi(\chi_1, \chi_2)$ grupe $G_p$

Od tod po preprostem računu določimo normo karakterja kot
```{math}
|| \chi_{\pi(\chi_1, \chi_2)} ||^2 = 
    \begin{cases}
        2 & \chi_1 = \chi_2, \\
        1 & \chi_1 \neq \chi_2.
    \end{cases}
```
Za $\chi_1 \neq \chi_2$ je upodobitev $\pi(\chi_1, \chi_2)$ torej nerazcepna. Iz karakterja opazimo, da je $\rho$ simetrična v svojih argumentih, se pravi $\pi(\chi_1, \chi_2) \cong \pi(\chi_2, \chi_1)$. Na ta način torej dobimo $\binom{p-1}{2} = (p-1)(p-2)/2$ nerazcepnih upodobitev grupe $G_p$. Tem upodobitvam pravimo <span class="definicija">upodobitve glavne vrste</span>.[^15] V primeru, ko je $\chi_1 = \chi_2$, iz vrednosti karakterjev opazimo izomorfizem $\pi(\chi, \chi) \cong \St(\chi) \oplus (\chi \circ \det)$, torej tukaj ne najdemo nobenih novih nerazcepnih upodobitev.

### Tabela karakterjev, 2. del

Opazujmo zdaj še upodobitve, ki jih dobimo z indukcijo iz nerazcepnega torusa. Te so nekoliko bolj zapletene, zato bomo pristopili bolj previdno. Naj bo
```{math}
\theta \colon T_{nr} \cong \FF_p(\sqrt{\epsilon})^* \to \CC^*
```
poljubna enorazsežna upodobitev. Izračunajmo karakter indukcije upodobitve $\theta$ nerazcepnega torusa. Uporabimo formulo za karakter inducirane upodobitve. Naj bo $R$ množica predstavnikov desnih odsekov $T_{nr}$ v $G_p$. Za $g \in G_p$ je $r g r^{-1} \in T_{nr}$ za nek $r \in R$, če in samo če je $r g r^{-1}$ bodisi skalar bodisi nerazcepen polenostaven element, kar je enakovredno temu, da je $g$ bodisi skalar bodisi nerazcepen polenostaven element. Za skalarje, ki jih interpretiramo kot elemente $g = a \in \FF_p^* \subseteq \FF_p(\sqrt{\epsilon})^*$, velja
```{math}
\textstyle \Ind_{T_{nr}}^{G_p}(\theta)(a) = |G_p : T_{nr}| \cdot \theta(a) = p(p-1) \theta(a).
```
Za nerazcepne polenostavne elemente, ki jih interpretiramo kot elemente $g = a + \sqrt{\epsilon} b \in \FF_p(\sqrt{\epsilon})^*$, pa velja $g^{G_p} \cap T_{nr} = \{ g, g^{\sigma} \}$. V formuli za izračun induciranega karakterja sta zato relevantna le dva člena in dobimo
```{math}
\textstyle \Ind_{T_{nr}}^{G_p}(\theta)(a + \sqrt{\epsilon} b) = \theta(a + \sqrt{\epsilon} b) + \theta(a - \sqrt{\epsilon} b).
```
Z avtomorfizmom $\sigma \in \Gal(\FF_p(\sqrt{\epsilon})/\FF_p)$ lahko delujemo na upodobitvi s predpisom $\theta^\sigma(x) = \theta(x^\sigma) = \theta(x^p)$. Torej je zadnja vrednost karakterja enaka $\theta(g) + \theta^\sigma(g)$.

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:--:|:--:|:--:|:--:|
| $\Ind_{T_{nr}}^{G_p}(\theta)$ | $p(p-1) \theta(a)$ | $0$ | $0$ | $\theta(a + \sqrt{\epsilon}b) + \theta(a - \sqrt{\epsilon}b)$ |

Karakter upodobitve $\Ind_{T_{nr}}^{G_p}(\theta)$ grupe $G_p$

Iz vrednosti karakterjev lahko izračunamo normo induciranega karakterja. Vrednost $|| \Ind_{T_{nr}}^{G_p}(\theta) ||^2$ je enaka
```{math}
\frac{1}{|G_p|} \left(  \sum_{g \in \FF_p^*} (p (p-1) |\theta(g)|)^2 + \sum_{g \in \FF_p(\sqrt{\epsilon})^* \backslash \FF_p^*} \frac{p(p-1)}{2} \cdot |\theta(g) + \theta^{\sigma}(g)|^2 \right).
```
Zadnjo vsoto lahko po razvoju kvadrata zapišemo kot
```{math}
\frac{p(p-1)}{2} \cdot \left( 2 (p^2  - p) + 2 \Realpart \left( \sum_{g \in \FF_p(\sqrt{\epsilon})^*} \theta(g) \overline{\theta^{\sigma}(g)} - \sum_{g \in \FF_p^*}  |\theta(g)|^2 \right) \right).
```
Prvo notranjo vsoto prepoznamo kot skalarni produkt upodobitev $\theta$ in $\theta^{\sigma}$ v grupi $\FF_p(\sqrt{\epsilon})$, ki je enak bodisi $0$ bodisi $1$ po ortogonalnosti nerazcepnih karakterjev. S tem je norma $|| \Ind_{T_{nr}}^{G_p}(\theta) ||^2$ enaka
```{math}
\frac{1}{|G_p|} \left( p^2(p-1)^3 + p^2(p-1)^2 + p(p-1) \cdot \left(  (p^2 - 1) \langle \theta, \theta^{\sigma} \rangle - (p-1) \right) \right),
```
kar se poenostavi do
```{math}
|| {\textstyle \Ind_{T_{nr}}^{G_p}(\theta)} ||^2 = p-1 + \langle \theta, \theta^{\sigma} \rangle = \begin{cases}
        p & \theta = \theta^\sigma, \\
        p-1 & \theta \neq \theta^{\sigma}.
    \end{cases}
```
Upodobitev $\Ind_{T_{nr}}^{G_p}(\theta)$ je torej daleč od nerazcepne.

Pred nadaljevanjem postojmo pri pogoju $\theta = \theta^{\sigma}$, ki razdeli inducirane upodobitve na dva naravna razreda. Ta pogoj lahko enakovredno zapišemo kot $\theta(x) = \theta(x^{p})$ za vsak $x \in \FF_p(\sqrt{\epsilon})^*$, kar je, ker je $\FF_p(\sqrt{\epsilon})^*$ ciklična grupa, enako kot $\theta(x^{p-1}) = 1$. Vrednost $\theta$ je torej trivialna na množici $\{ x^{p-1} \mid x \in \FF_p(\sqrt{\epsilon})^* \}$, ki jo prepoznamo ravno kot jedro determinante $\ker(\det) = \{ x \in \FF_p(\sqrt{\epsilon})^* \mid x^{p+1} = 1 \}$. Pogoj $\theta = \theta^{\sigma}$ je torej enakovreden temu, da se $\theta$ *faktorizira prek determinante*, se pravi da je oblike $\theta = \chi \circ \det$ za nek karakter $\chi \colon \FF_p^* \to \CC^*$. Vseh takih upodobitev je $p-1$. Upodobitve $\theta$, ki se *ne* faktorizirajo prek determinante, torej za katere velja $\theta \neq \theta^{\sigma}$, se imenujejo <span class="definicija">regularne</span>. Regularne upodobitve prihajajo torej v parih $(\theta, \theta^\sigma)$. Število Galoisjevih orbit regularnih upodobitev je zato enako $((p^2 - 1) - (p-1))/2 = p(p-1)/2$.

Glede na to, da inducirana upodobitev iz nerazcepnega torusa ni nerazcepna, lahko poskusimo inducirati še iz kakšne druge podgrupe. Naravni kandidat, ki nam še preostane, je centralizator nediagonalizabilnega elementa, se pravi grupa $C_p = S_p \times U_p$. Izberimo upodobitvi
```{math}
\chi \colon S_p \cong \FF_p^* \to \CC^*, \quad
    \psi \colon U_p \cong \FF_p \to \CC^*
```
in tvorimo produktno upodobitev $\chi \times \psi$ grupe $C_p$. To upodobitev induciramo na grupo $G_p$. S formulo za izračun karakterjev inducirane upodobitve ni težko določiti njenega karakterja. Naj bo $R$ množica predstavnikov desnih odsekov $C_p$ v $G_p$. Za $g \in G_p$ je $r g r^{-1} \in C_p$ za nek $r \in R$, če in samo če je $g$ bodisi skalar bodisi nediagonalizabilen element. Za skalarje velja
```{math}
{\textstyle \Ind_{C_p}^{G_p}(\chi \times \psi) } \left( \begin{pmatrix} a & 0 \\ 0 & a \end{pmatrix} \right)
    = |G_p : C_p| \cdot \chi(a) = (p^2 - 1) \chi(a).
```
Za nediagonalizabilen element $g$ pa velja $g^{G_p} \cap C_p = g U_p \backslash S_p$, zato je v formuli za induciran karakter relevantnih le $p-1$ členov in dobimo
```{math}
{\textstyle \Ind_{C_p}^{G_p}(\chi \times \psi)} \left( \begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix} \right)
    = \sum_{t \in \FF_p^*} (\chi \times \psi) \left( \begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix} \cdot \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} \right)
    = \sum_{t \in \FF_p^*} \chi(a) \psi(t).
```
Zadnjo vsoto lahko prepišemo kot
```{math}
\chi(a) \cdot \left( \sum_{t \in \FF_p} \psi(t) - 1 \right)
    = \chi(a) \cdot \left( p \cdot \langle \psi, \oneone \rangle - 1 \right)
    = \begin{cases}
        (p-1) \chi(a) & \psi = \oneone, \\
        - \chi(a) & \psi \neq \oneone.
    \end{cases}
```
Inducirani karakter je torej odvisen od $\psi$ le preko veljavnosti enakosti $\psi = \oneone$.

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:--:|:--:|:--:|:--:|
| $\Ind_{C_p}^{G_p}(\chi \times \psi)$ | $(p^2 - 1) \chi(a)$ | $(p \cdot 1_{\psi = \oneone} - 1) \chi(a)$ | $0$ | $0$ |

Karakter upodobitve $\Ind_{C_p}^{G_p}(\chi \times \psi)$ grupe $G_p$

Iz vrednosti karakterjev izračunamo normo
```{math}
||{\textstyle \Ind_{C_p}^{G_p}(\chi \times \psi)} ||^2
    = \begin{cases}
        2(p-1) & \psi = \oneone, \\
        p & \psi \neq \oneone.
    \end{cases}
```
Upodobitev $\Ind_{C_p}^{G_p}(\chi \times \psi)$ je torej spet daleč od nerazcepne.

Primerjajmo obe inducirani upodobitvi. Skalarni produkt njunih karakterjev lahko izračunamo tako, da seštejemo le prispevke po skalarnih elementih, saj so vsi ostali členi ničelni. Dobimo
```{math}
{\textstyle \langle \Ind_{T_{nr}}^{G_p}(\theta), \Ind_{C_p}^{G_p}(\chi \times \psi) \rangle}
= \frac{1}{|G_p|} \sum_{a \in \FF_p^*} p(p-1) \theta(a) \cdot (p^2 - 1) \overline{\chi(a)},
```
kar prepoznamo kot
```{math}
(p-1) \cdot \langle \theta |_{S_p}, \chi \rangle 
= \begin{cases}
        0 & \chi \neq \theta |_{S_p}, \\
        p-1 & \chi = \theta |_{S_p}. \\
\end{cases}
```
Če torej izberemo $\chi = \theta |_{S_p}$, je skalarni produkt med obema upodobitvama enak $p-1$. Izračunali smo tudi že normi obeh upodobitev, obe sta blizu $\sqrt{p}$. V luči Cauchy-Schwartzove neenakosti sta karakterja obeh induciranih upodobitev kot vektorja torej zelo blizu temu, da bi bila *vzporedna* in s tem *enaka*. Najtesnejšo zvezo med njima dobimo, če minimiziramo normi obeh, torej če vzamemo za $\theta$ regularen karakter in za $\psi$ poljuben netrivialen karakter. S to izbiro opazujmo *virtualen* karakter
```{math}
\textstyle \zeta_{\theta} = \Ind_{C_p}^{G_p}(\theta |_{S_p} \times \psi) - \Ind_{T_{nr}}^{G_p}(\theta) \in R(G_p).
```
Po že opravljenih računih je norma tega virtualnega karakterja res minimalna,
```{math}
\textstyle \langle \zeta_{\theta}, \zeta_{\theta} \rangle 
    = ||\Ind_{C_p}^{G_p}(\theta |_{S_p} \times \psi)||^2 + ||\Ind_{T_{nr}}^{G_p}(\theta)||^2 - 2 \langle \Ind_{T_{nr}}^{G_p}(\theta), \Ind_{C_p}^{G_p}(\theta |_{S_p} \times \psi) \rangle = 1.
```
Torej je bodisi $\zeta_{\theta}$ bodisi $-\zeta_{\theta}$ nerazcepen karakter. Ker velja $\zeta_{\theta}(1) = p-1$, je $\zeta_{\theta}$ nerazcepen karakter.

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:--:|:--:|:--:|:--:|
| $\zeta_{\theta}$ | $(p-1) \theta(a)$ | $-\theta(a)$ | $0$ | $- \theta(a + \sqrt{\epsilon} b) - \theta(a - \sqrt{\epsilon} b)$ |

Karakter $\zeta_{\theta}$ grupe $G_p$

Na ta način za vsak regularen karakter $\theta$ nerazcepnega torusa dobimo nerazcepno upodobitev s karakterjem $\zeta_{\theta}$. Taki upodobitvi pravimo <span class="definicija">ostna upodobitev</span>.[^16] Z izračunom skalarnih produktov se ni težko prepričati, da sta dve taki upodobitvi izomorfni, če in samo če sta regularna karakterja v isti orbiti Galoisjeve grupe. Število ostnih upodobitev je zato enako $p(p-1)/2$. Poudarimo, da smo ostne upodobitve konstruirali le implicitno prek indukcij. Z nekaj truda bi lahko izpeljali eksplicitno konstrukcijo teh upodobitev. Izkaže se, da ostnih upodobitev *ni* mogoče opisati kot neposredno induciranih iz podgrup $G_p$.[^17]

Povzemimo. Skupaj smo našli naslednje upodobitve:

- linearne: $p-1$ upodobitev stopnje $1$,

- Steinbergove: $p-1$ upodobitev stopnje $p$,

- glavne vrste: $(p-1)(p-2)/2$ upodobitev stopnje $p+1$,

- ostne: $p(p-1)/2$ upodobitev stopnje $p-1$.

S tem smo našteli $p^2-1$ nerazcepnih upodobitev in zatorej vse nerazcepne upodobitve grupe $G_p$.

|  | $\mat{a}{0}{0}{a}$ | $\mat{a}{1}{0}{a}$ | $\mat{a}{0}{0}{b}$ | $\mat{a}{\epsilon b}{b}{a}$ |
|:---|:---|:---|:---|:---|
| $\chi \circ \det$ | $\chi(a)^2$ | $\chi(a)^2$ | $\chi(a) \chi(b)$ | $\chi(a^2 - \epsilon b^2)$ |
| $\St(\chi)$ | $p \chi(a)^2$ | $0$ | $\chi(a) \chi(b)$ | $- \chi(a^2 - \epsilon b^2)$ |
| $\pi(\chi_1, \chi_2)$ | $(p+1) \chi_1(a) \chi_2(a)$ | $\chi_1(a) \chi_2(a)$ | $\chi_1(a) \chi_2(b) + \chi_2(a) \chi_1(b)$ | $0$ |
| $\zeta_{\theta}$ | $(p-1) \theta(a)$ | $-\theta(a)$ | $0$ | $- \theta(a + \sqrt{\epsilon} b) - \theta(a - \sqrt{\epsilon} b)$ |

Tabela karakterjev $G_p$

Izračunano tabelo karakterjev grupe $G_p$ lahko uporabimo, da z njo določimo še tabelo karakterjev grupe $\PSL_2(\FF_p)$.

<div class="domacanaloga">

Izračunaj tabelo karakterjev grupe $\SL_2(\FF_p)$ in grupe $\PSL_2(\FF_p)$. S tabelo se prepričaj, da je grupa $\PSL_2(\FF_p)$ enostavna za $p > 3$. V pomoč ti je lahko obravnava v (Fulton-Harris 2004).

</div>

### Matrike višjih razsežnosti

Argumente, ki smo jih videli v tem razdelku, bi lahko posplošili na matrike večjih razsežnosti in tako (s precej več truda) izračunali generično tabelo karakterjev grupe $\GL_n(\FF_q)$, kot je storil [(Green 1955)](https://www.jstor.org/stable/1992997#metadata_info_tab_contents). Zopet dobimo glavno vrsto upodobitev, tokrat inducirano induktivno iz podgrup $\GL_m(\FF_q)$ za $m < n$. Pri tem je relevantno, da to lahko naredimo na več načinov, na primer za vsako razčlenitev števila $n = m_1 + m_2 + \cdots + m_k$ lahko v $\GL_n(\FF_q)$ vidimo bločno diagonalni direktni produkt grup
```{math}
\textstyle  \GL_{m_1}(\FF_q) \times \GL_{m_2}(\FF_q) \times \cdots \times \GL_{m_k}(\FF_q).
```
Teorija upodobitev $\GL_n(\FF_q)$ zato vključuje nekaj kompleksnosti teorije upodobitev simetrične grupe $S_n$. Tudi v splošnem primeru dobimo ostne upodobitve, in sicer s pomočjo indukcije iz Galoisjevih razredov regularnih upodobitev nerazcepnega torusa, ki ga lahko predstavimo kot končno polje $\FF_{q^n}$.

Ni pa tako enostavno pridobiti tudi tabele karakterjev družine enostavnih grup $\PSL_n(\FF_q)$ ali njene prijateljice $E_8(\FF_q)$. Seveda lahko posamezne tabele za specifične vrednosti $n$ in $q$ izračunamo,[^18] ampak končni cilj je imeti generične tabele karakterjev, kot smo to dosegli za $G_p = \GL_2(\FF_p)$. Za razumevanje teorije upodobitev teh grup imamo na voljo matematično zahtevno [Deligne-Lusztigovo teorijo](https://en.wikipedia.org/wiki/Deligne–Lusztig_theory), ki upodobitve končnih grup sestavlja s pomočjo upodobitev prirejenih algebraičnih grup nad algebraično zaprtim poljem, na primer $\SL_n(\overline{\FF_p})$, in sicer te upodobitve izhajajo iz delovanja na $\ell$-adičnih kohomoloških grupah prirejenih raznoterosti. Iz te teorije lahko razumemo *del* generične tabele karakterjev, na primer poznamo vse stopnje nerazcepnih upodobitev, ne poznamo pa vseh vrednosti vseh karakterjev.

[^1]: Na primer abelove grupe, simetrične grupe, diedrske grupe, splošne linearne grupe, končne enostavne grupe, …

[^2]: Vsaka končna grupa je zgrajena iz končnih enostavnih grup, te pa sestojijo iz, grobo rečeno, treh neskončnih družin, in sicer cikličnih grup praštevilske moči $\ZZ/p\ZZ$, alternirajočih grup $A_n$ in različnih matričnih grup nad končnimi polji, na primer $\SL_n(\FF_p)/Z(\SL_n(\FF_p))$. Zgleda družin, ki si jih bomo ogledali, sta torej do neke mere reprezentativna za razumevanje upodobitev nekomutativnih končnih enostavnih grup. Podrobnejši opis končnih enostavnih grup je na voljo [tukaj](https://en.wikipedia.org/wiki/List_of_finite_simple_groups).

[^3]: Res, če je $x = q_1 p_1 = q_2 p_2$, potem je $q_2^{-1} q_1 = p_2 p_1^{-1} \in P \cap Q = 1$, zato je $q_1 = q_2$ in $p_1 = p_2$.

[^4]: Ker je $\Fcal(\youngsym)$ spletična, je to res invarianten podprostor. Ni pa težko videti, kako elementi grupe zares delujejo; za $g \in S_n$ element $\rho_{\fun}(g)$ preslika $\youngsym * f$ v $\youngsym * (\rho_{\fun}(g) \cdot f)$.

[^5]: Velja namreč $\youngsym/n_{\lambda} * \youngsym/n_{\lambda} * f = \youngsym/n_{\lambda} * f$.

[^6]: Če izbrana baza ni ortogonalna, na njej uporabimo Gram-Schmidtovo ortogonalizacijo.

[^7]: Na primer, mnogo dela je osredotočenega na [Lusztigovo in Jamesovo domnevo](https://mathoverflow.net/questions/138310/what-to-do-now-that-lusztigs-and-james-conjectures-have-been-shown-to-be-false).

[^8]: $H_{\lambda}(i,j)$ torej sestoji iz tistih celic $(a,b)$, za katere je $a = i$ in $b \geq j$ ali $b = j$ in $a \geq i$.

[^9]: Lastnosti, ki jih bomo navedli v tem razdelku, ni težko preveriti in jih prepuščamo bralcu v razmislek.

[^10]: Ponovljena ničla bi bila ničla odvoda karakterističnega polinoma, ki pa je linearen in ima vse ničle v $\FF_p$.

[^11]: Če zamenjamo v zgornji matriki $b$ z $-b$, dobimo podobno matriko. To ravno ustreza delovanju $\sigma$.

[^12]: Za funkciji $f,g \colon \NN \to \RR$ pišemo $f \sim g$, če velja $\lim_{n \to \infty} f(n)/g(n) = 1$.

[^13]: Element $x + \sqrt{\epsilon} y$ deluje na $\FF_p(\sqrt{\epsilon})$ z množenjem z leve. Če to grupo obravnavamo kot vektorski prostor nad $\FF_p$, potem je matrika tega delovanja v bazi $\{ 1, \sqrt{\epsilon} \}$ ravno ta, ki je prikazana.

[^14]: Steinbergovo upodobitev dobimo torej tako, da $\Pi$ podaljšamo s standardno upodobitvijo simetrične grupe $S_{p+1}$.

[^15]: Angleško *principal series representations*.

[^16]: Angleško *cuspidal representation*.

[^17]: Najpreprostejši znan opis je preko Weilove upodobitve (Bushnell-Henniart 2006), ki ostne upodobitve uresniči na določenih podprostorih v $\fun(\FF_p(\sqrt{\epsilon}), \CC)$.

[^18]: Računanje teh tabel specifičnih končnih enostavnih grup je zbrano v [ATLAS](http://brauer.maths.qmul.ac.uk/Atlas/v3/). Ti izračuni so močno pripomogli k dokazu izreka o [klasifikaciji končnih enostavnih grup](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups).


## Kviz

```{raw} html
<div class="quiz-item" data-correct="true">
```

Nerazcepne kompleksne upodobitve $S_n$ so v bijekciji z razčlenitvami $\lambda$ števila $n$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Vektorskemu prostoru $V_{\lambda}$, prirejenemu razčlenitvi $\lambda$, pravimo Špelin modul.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Razčlenitvi $(n-1,1)$ števila $n$ ustreza standardna upodobitev $S_n$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Iz vsake nerazcepne upodobitve $S_n$ lahko po izbiri ustrezne baze s projekcijo mod $p$ dobimo modularno upodobitev.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Vrednosti nerazcepnih karakterjev simetrične grupe lahko izračunamo s Frobeniusovo formulo.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Formula o dolžinah kljuk pove, da lahko vrednosti nerazcepnih karakterjev izračunamo iz dolžin kljuk v diagramu razčlenitve.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Vsaka nerazcepna upodobitev alternirajoče grupe $A_n$  je restrikcija nerazcepne updobitve simetrične grupe $S_n$.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Podgrupa zgornjetrikotnih matrik v $G_p = GL_2(\mathbf{F}_p)$ se imenuje Boreliozna podgrupa.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Grupa $G_p$ naravno deluje na projektivni premici nad končnim poljem.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Za $p > 3$ je grupa $PSL_2(\mathbf{F}_p)$ enostavna.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Razcepni in nerazcepni torus v $GL_2(\mathbf{F}_p)$ sta kot abelovi grupi izomorfna.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="true">
```

Steinbergova upodobitev je nerazcepna upodobitev $GL_2(\mathbf{F}_p)$, ki je podupodobitev permutacijske upodobitve $GL_2(\mathbf{F}_p)$ na projektivni premici.

```{raw} html
</div>
```

```{raw} html
<div class="quiz-item" data-correct="false">
```

Nerazcepne upodobitve grupe $GL_2(\mathbf{F}_p)$, ki jih dobimo z indukcijo iz podgrupe zgornjetrikotnih matrik, se imenujejo upodobitve sekundarne vrste.

```{raw} html
</div>
```
