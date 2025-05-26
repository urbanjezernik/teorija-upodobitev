```{raw} html
<style>
  body { counter-reset: chapter 1 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Upodobitev pod mikroskopom

V tem poglavju bomo pribili upodobitev dane grupe in se ji tesno približali, kot da bi jo pogledali pod mikroskopom. Pri tem bomo najprej uzrli osnovne kose, iz katerih je sestavljena upodobitev. Ti osnovni kosi ustrezajo celicam, ki jih vidimo pod mikroskopom. Za tem se bomo približali še sestavi teh osnovnih kosov: vsak je dan s homomorfizmom v matrike, zato bomo raziskali koeficiente te matrike. Ti ustrezajo organelom, ki jih v celici vidimo pod mikroskopom. Nazadnje bomo premislili, da so te upodobitvene celice dovolj diferencirane med sabo, da za njihovo identifikacijo zadošča poznavanje le nekaterih njihovih organelov.

## Razstavljanje upodobitve

Pogosto nas zanima, ali lahko dano upodobitev $\rho$ grupe $G$ na prostoru $V$ zapišemo kot direktno vsoto nekih podupodobitev in na ta način upodobitev $\rho$ *razstavimo* na preprostejše upodobitve, podobno kot razstavimo števila na manjše faktorje.

### Nerazcepnost

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V \neq 0$. Kadar *ne* obstaja noben $G$-invarianten podprostor prostora $V$ (razen prostorov $0$ in $V$), tedaj rečemo, da je upodobitev $\rho$ <span class="definicija">nerazcepna</span>.[^1] V tem primeru upodobitve seveda ne moremo razstaviti na enostavnejše v smislu direktne vsote.

<div class="zgled">

- Opazujmo permutacijsko upodobitev simetrične grupe $S_3$ na prostoru $\RR[\{ 1,2,3 \}] = \RR^3$. Premislili smo že, da je ta upodobitev direktna vsota enorazsežne podupodobitve $\oneone$ in dvorazsežne podupodobitve $\rho$, pri čemer slednja nima nobene enorazsežne podupodobitve. S tem je permutacijska upodobitev razstavljena kot direktna vsota dveh nerazcepnih upodobitev.

- Opazujmo diedrsko grupo $D_{2n}$ z dvorazsežno upodobitvijo $\rho_k$ za $k \in \ZZ$, ki jo obravnavajmo kot kompleksno upodobitev. Matrika $\rho_k(r)$ ima lastni vrednosti $e^{\pm 2 \pi i k / n}$. Ti dve vrednosti sta različni, če in samo če $k$ *ni* deljiv z $n/2$. Za vsak $0 < k < n/2$ ima $\rho_k(r)$ torej različni lastni vrednosti z lastnima vektorjema $\left( \begin{smallmatrix} 1 \\ \mp i \end{smallmatrix} \right)$. Matrika $\rho_k(s)$ zamenja ta dva lastna podprostora med sabo. Upodobitev $\rho_k$ za $0 < k < n/2$ torej nima nobene enorazsežne kompleksne podupodobitve in je zato nerazcepna.

</div>

Preverimo, da so nerazcepne upodobitve dane grupe med sabo *neprimerljive*, tudi če so enake razsežnosti. Zatorej si jih lahko predstavljamo kot neodvisne osnovne kose kategorije upodobitev dane grupe.[^2]

<div class="lema">

Naj bo $G$ grupa z upodobitvijo $\rho$ in nerazcepno upodobitvijo $\pi$. Tedaj je vsaka spletična v $\hom_G(\pi, \rho)$ bodisi injektivna bodisi ničelna in vsaka spletična v $\hom_G(\rho, \pi)$ je bodisi surjektivna bodisi ničelna. V posebnem je vsaka spletična med dvema nerazcepnima upodobitvama grupe $G$ bodisi izomorfizem bodisi ničelna.

</div>

<div class="dokaz">

Naj bo $\Phi \in \hom_G(\pi, \rho)$. Tedaj je $\ker \Phi$ podupodobitev $\pi$, zato je po nerazcepnosti bodisi $\ker \Phi = 0$ bodisi $\Phi = 0$. Prvi primer ustreza možnosti, da je $\Phi$ injektivna, v drugem primeru pa je $\Phi$ ničelna. Soroden razmislek dokaže trditev o spletičnah v $\hom_G(\rho, \pi)$.

</div>

Nad algebraično zaprtimi polji lahko to neprimerljivost raztegnemo do ene same upodobitve: osnovni kosi nimajo netrivialnih simetrij.

<div class="posledica">

Naj bo $G$ grupa z nerazcepno upodobitvijo $\pi$ končne razsežnosti nad *algebraično zaprtim poljem*. Tedaj je $\dim \hom_G(\pi, \pi) = 1$. Povedano še drugače: množica $\hom_G(\pi, \pi)$ sestoji le iz skalarnih večkratnikov identitete.

</div>

<div class="dokaz">

Naj bo $0 \neq \Phi \in \hom_G(\pi, \pi)$. Ker je polje algebraično zaprto, ima linearna preslikava $\Phi$ vsaj kakšno lastno vrednost, recimo $\lambda$. Preslikava $\Phi - \lambda \cdot \id \in \hom_G(\pi, \pi)$ zato ni injektivna, s čimer mora biti po Schurovi lemi ničelna, se pravi $\Phi = \lambda \cdot \id$.

</div>

Množico vseh izomorfnostnih razredov nerazcepnih upodobitev dane grupe $G$ označimo z $\Irr(G)$.

<div class="zgled">

Naj bo $G$ grupa z nerazcepno upodobitvijo $\pi$ končne razsežnosti nad poljem kompleksnih števil. Spletične $\hom_G(\pi, \pi) = \hom(\pi, \pi)^G$ so endomorfizmi vektorskega prostora, ki so $G$-invariantni, se pravi komutirajo z delovanjem grupe $G$. Zglede takih endomorfizmov lahko dobimo iz delovanj centralnih elementov grupe $G$; za vsak $z \in Z(G)$ je $\pi(z) \in \hom_G(\pi, \pi)$. Po Schurovi lemi je zato $\pi(z) = \omega(z) \cdot \id$ za nek skalar $\omega(z)$. Ker je $\pi$ homomorfizem, je $\omega \colon Z(G) \to \CC^*$ enorazsežna upodobitev centra grupe $G$. Tej upodobitvi rečemo <span class="definicija">centralni karakter</span> upodobitve $\pi$.

Še posebej zanimiv je primer, ko je $G$ *abelova* grupa. Takrat za vsako nerazcepno upodobitev $\pi$ končne razsežnosti nad poljem $\CC$ velja $\pi(g) = \omega(g) \cdot \id$ za *vsak* $g \in G$. Vsak enorazsežen podprostor je zato avtomatično podupodobitev. Ker je $\pi$ nerazcepna, od tod sklepamo $\deg(\pi) = 1$ in s tem $\pi = \omega$. Upodobitev $\pi$ je tako *enorazsežna*. Na primer, vsaka končnorazsežna nerazcepna kompleksna upodobitev grupe $\RR$ je nujno enorazsežna.

</div>

<div class="domacanaloga">

Poišči kakšno nerazcepno upodobitev ciklične grupe $\ZZ/3\ZZ$ nad poljem $\QQ$, ki *ni* enorazsežna.

</div>

### Komplementarna podupodobitev

Predpostavimo zdaj, da ima dana upodobitev $\rho$ grupe $G$ na prostoru $V$ neko podupodobitev $\tilde\rho$ na podprostoru $W \leq V$. Seveda lahko vselej najdemo vektorski prostor $U \leq V$, za katerega je $V = U \oplus W$, vsekakor pa ni jasno, če lahko najdemo tak podprostor $U$, ki je celo $G$-invarianten. Kadar je temu tako, rečemo, da smo našli <span class="definicija">komplementarno podupodobitev</span> podupodobitve $\tilde\rho$.[^3] Ni vsaka podupodobitev komplementirana.

<div class="zgled">

Naj grupa $\RR$ deluje na realnem prostoru $\RR^2$ s homomorfizmom
```{math}
\rho \colon \RR \to {\textstyle \GL_2(\RR)}, \quad
        x \mapsto 
        \begin{pmatrix} 
        1 & x \\ 0 & 1 
    \end{pmatrix}.
```
Oglejmo si enorazsežne podupodobitve. Premislili smo že, da te ustrezajo skupnim lastnim vektorjem vseh preslikav $\rho(x)$ za $x \in \RR$. Pri $x = 1$ imamo linearno preslikavo $\rho(1)$ z enim samim lastnim vektorjem, in sicer $e_1 \in \RR^2$. Hkrati je $e_1$ lastni vektor vseh preslikav $\rho(x)$ za $x \in \RR$. Torej ima $\rho$ *eno samo* enorazsežno podupodobitev, in sicer je to $\RR \cdot e_1 \leq \RR^2$. Ta vektorski podprostor ima mnogo komplementov v $\RR^2$, noben od teh pa ni hkrati enorazsežna podupodobitev $\rho$.

</div>

Ni težko preveriti, da obstoj komplementarne podupodobitve vselej izhaja iz <span class="definicija">projekcijskih spletičen</span>.[^4]

<div class="trditev">

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$ in naj bo $\tilde \rho$ njena podupodobitev na prostoru $W \leq V$. Tedaj ima $\tilde \rho$ komplementarno podupodobitev, če in samo če obstaja spletična $\Phi \in \hom_G(V,V)$, ki je projekcija na $W$. V tem primeru je $\ker \Phi$ komplementarna upodobitev.

</div>

### Polenostavnost

Vrnimo se k začetni ideji o *razstavljanju* dane upodobitve. Kadar lahko dano upodobitev $\rho$ zapišemo kot direktno vsoto *nerazcepnih* upodobitev $\bigoplus_{i \in I} \rho_i$, tedaj rečemo, da je $\rho$ <span class="definicija">polenostavna</span> upodobitev. Če so pri tem vse podupodobitve $\rho_i$ izomorfne med sabo, upodobitev $\rho$ imenujemo <span class="definicija">izotipična</span> upodobitev.

<div class="zgled">

- Permutacijska upodobitev grupe $S_3$ na $\RR^3$ je polenostavna.

- Regularna upodobitev ciklične grupe $\ZZ/n\ZZ$ nad $\CC$ je polenostavna.

</div>

Vseh upodobitev žal ne moremo razstaviti na direktno vsoto nerazcepnih.[^5] Polenostavnost dane upodobitve je namreč tesno povezana z obstojem komplementarnih podupodobitev.

<div class="trditev">

Upodobitev grupe $G$ je polenostavna, če in samo če ima vsaka njena podupodobitev komplementarno podupodobitev.

</div>

<div class="dokaz">

$(\Rightarrow)$: Naj bo najprej $\rho \colon G \to \GL(V)$ polenostavna upodobitev, pri kateri je $V = \bigoplus_{i \in I} V_i$ in upodobitve $G$ na podprostorih $V_i$ so nerazcepne. Naj bo $W \leq V$ poljuben $G$-invarianten podprostor. Po Zornovi lemi obstaja maksimalen $G$-invarianten podprostor $U \leq V$ z lastnostjo $U \cap W = 0$. Izberimo poljuben $i \in I$. Presek $(U \oplus W) \cap V_i$ je $G$-invarianten podprostor prostora $V_i$, zato je po nerazcepnosti bodisi trivialen bodisi enak $V_i$. Če bi bil trivialen, bi lahko $U$ povečali do prostora $U \oplus V_i$, kar je v nasprotju z maksimalnostjo izbire $U$. Zatorej je $(U \oplus W) \cap V_i = V_i$ in tako $(U \oplus W) \geq V_i$. Ker je bil $i$ poljuben, od tod sledi $U \oplus W = V$. Podupodobitev $W$ ima torej komplementarno podupodobitev $U$.

$(\Leftarrow)$: Naj bo $\rho \colon G \to \GL(V)$ upodobitev, v kateri je vsaka podupodobitev komplementirana. Dokazati želimo, da je $\rho$ polenostavna. Uporabili bomo naslednjo pomožno trditev, ki je ni težko preveriti.

<div class="domacanaloga">

Naj bo $\rho$ upodobitev, v kateri je vsaka podupodobitev komplementirana. Tedaj ima $\rho$ nerazcepno podupodobitev.

</div>

Naj bo $W$ vsota vseh $G$-invariantnih podprostorov v $V$, ki so nerazcepne upodobitve, se pravi $W = \sum_{i \in I} V_i$, a ta vsota ni nujno direktna. Po pomožni trditvi je $W \neq 0$. Po predpostavki je $W$ komplementirana z $G$-invariantnim podprostorom $U$. Po pomožni trditvi ima tudi $U$ nerazcepno podupodobitev, zato je ta vsebovana v $W$, kar implicira $W = V$. Dokažimo zdaj še, da je $W$ *direktna* vsota podprostorov $V_i$. V ta namen naj bo $J$ maksimalna podmnožica indeksne množice $I$, za katero je $\sum_{j \in J} V_j$ direktna vsota. Taka podmnožica obstaja po Zornovi lemi. Označimo $\tilde V = \bigoplus_{j \in J} V_j$. Če velja $\tilde V \neq V$, potem mora za nek $i \in I \backslash J$ po nerazcepnosti veljati $V_i \cap \tilde V = 0$, kar pa je v nasprotju z maksimalnostjo množice $J$. Tako je res $\tilde V = V$ in upodobitev $V$ je polenostavna.

</div>

<div class="zgled">

Eničnozgornjetrikotna upodobitev grupe $\RR$ na $\RR^2$ *ni* nerazcepna, hkrati pa njena podupodobitev $\RR \cdot e_1 \cong \oneone$ *ni* komplementirana. Ta upodobitev zatorej *ni* polenostavna.

</div>

Z uporabo zadnjega kriterija lahko dokažemo, da je polenostavnost zaprta za osnovne konstrukcije z upodobitvami.

<div class="posledica">

Podupodobitve, kvocienti in direktne vsote polenostavnih upodobitev dane grupe so polenostavne.

</div>

<div class="dokaz">

Preverimo le zaprtost za podupodobitve. Naj bo $\rho$ polenostavna upodobitev grupe $G$ na prostoru $V$ in naj bo $W \leq V$ podupodobitev. Naj bo $U \leq W$ poljubna podupodobitev upodobitve na $W$. Po polenostavnosti obstaja komplementarna podupodobitev $\tilde U \leq V$ upodobitve $U \leq V$. Tedaj je $\tilde U \cap W$ podupodobitev, ki je komplementirana podupodobitvi $U$ v $W$.

</div>

Nazadnje lahko s pomočjo projekcijskih spletičen naredimo še en korak naprej pri razumevanju simetrij upodobitev. Premislili smo že, da so osnovni kosi brez netrivialnih simetrij. V primeru polenostavnih upodobitev drži tudi obratno.

<div class="posledica">

Naj bo $G$ grupa s *polenostavno* upodobitvijo $\rho$ končne razsežnosti. Če je $\dim \hom_G(\rho, \rho) = 1$, potem je $\rho$ nerazcepna.

</div>

<div class="dokaz">

Naj $\rho$ upodablja grupo $G$ na prostoru $V$. Naj bo $W \leq V$ nerazcepna podupodobitev in naj bo $U$ njena komplementarna podupodobitev. Naj bo $\Phi \colon V \to V$ pripadajoča projekcija na podprostor $W$ z jedrom $U$. Ker je $\Phi \in \hom_G(\rho, \rho)$, iz predpostavke sledi, da je $\Phi$ skalarni večkratnik identitete. To je mogoče le v primeru, ko je $V = W$ in $U = 0$, torej je $\rho$ nerazcepna.

</div>

### Kompozicijska vrsta

Vsake upodobitve ne moremo razstaviti kot direktno vsoto nerazcepnih upodobitev. Kljub temu pa je res, da lahko vsako upodobitev (na končnorazsežnem prostoru) razstavimo na nerazcepne upodobitve, le da moramo pri tem poseči po nekoliko zahtevnejšem načinu razstavljanja.

Naj bo $G$ grupa z upodobitvijo na prostoru $V$. Predpostavimo, da obstaja zaporedje $G$-invariantnih podprostorov
```{math}
0 = V_0 \leq V_1 \leq V_2 \leq \cdots \leq V_n = V,
```
pri čemer so vsi zaporedni kvocienti $V_i/V_{i-1}$ za $1 \leq i \leq n$, gledani kot upodobitve grupe $G$, *nerazcepni*. Tako zaporedje imenujemo <span class="definicija">kompozicijska vrsta</span> upodobitve na prostoru $V$. Kvocienti $V_i/V_{i-1}$ se pri tem imenujejo <span class="definicija">kompozicijski faktorji</span>.

<div class="zgled">

Naj bo $\rho$ eničnozgornjetrikotna upodobitev grupe $\RR$ na $V = \RR^2$. Ta upodobitev ima podupodobitev $V_1 = \RR \cdot e_1$. Kvocient $V/V_1$ je enorazsežen in na njem grupa $\RR$ deluje trivialno. Dobimo torej kompozicijsko vrsto
```{math}
0 = V_0 \leq V_1 \leq V,
```
katere kompozicijska faktorja sta kot upodobitvi izomorfna $\oneone$. Sama upodobitev grupe $\RR$ na $V$ pa seveda ni trivialna.

</div>

<div class="izrek">

Vsaka upodobitev na končnorazsežnem prostoru ima kompozicijsko vrsto. Vsaki dve kompozicijski vrsti imata enako število členov in do permutacije ter izomorfizma natančno enake kompozicijske faktorje.

</div>

<div class="dokaz">

Naj grupa deluje linearno na končnorazsežnem prostoru $V$. Da kompozicijska vrsta res obstaja, ni težko preveriti. Najprej izberemo neko nerazcepno podupodobitev $V_1$. Če je $V_1 < V$, potem izberemo podupodobitev $V_2$, ki vsebuje $V_1$ in je med vsemi takimi minimalne razsežnosti. S tem je $V_2/V_1$ nerazcepna. Induktivno nadaljujemo z grajenjem kompozicijske vrste. Ker je $V$ končnorazsežen, se ta postopek ustavi.

Premislimo še, kako lahko vsaki dve kompozicijski vrsti povežemo med sabo. Opazujmo dve taki vrsti,
```{math}
0 = V_0 \leq V_1 \leq \cdots \leq V_n = V 
    \quad \text{in} \quad
    0 = W_0 \leq W_1 \leq \cdots \leq W_m = V.
```
S pomočjo druge vrste bomo skušali *pofiniti* prvo vrsto in obratno.[^6] Za $0 \leq i < n$ in $0 \leq j \leq m$ naj bo
```{math}
V_{i,j} = V_i + (V_{i+1} \cap W_j),
```
S tem dobimo verigo
```{math}
V_i = V_{i,0} \leq V_{i,1} \leq \cdots \leq V_{i,m} = V_{i+1}
```
med $V_i$ in $V_{i+1}$. Ker je kvocient $V_{i+1}/V_i$ nerazcepen in je vsak $V_{i,j}$ podupodobitev, mora za natanko en indeks $j$ veljati $V_i = V_{i,j}$ in $V_{i+1} = V_{i,j+1}$. Kompozicijski faktor $V_{i+1}/V_i$ je tedaj izomorfen kvocientu
```{math}
\frac{V_i + (V_{i+1} \cap W_{j+1})}{V_i + (V_{i+1} \cap W_j)}.
```
Zgodbo zdaj ponovimo še za drugo verigo. Pofinimo jo s pomočjo prve, definiramo $W_{j,i} = W_j + (W_{j+1} \cap V_i)$. Kvocient $W_{j+1}/W_j$ je enak
```{math}
\frac{W_j + (W_{j+1} \cap V_{i+1})}{W_j + (W_{j+1} \cap V_i)}.
```

<div class="domacanaloga">

Prepričaj se, da velja
```{math}
\frac{V_i + (V_{i+1} \cap W_{j+1})}{V_i + (V_{i+1} \cap W_j)}
    \cong
    \frac{W_j + (W_{j+1} \cap V_{i+1})}{W_j + (W_{j+1} \cap V_i)}.
```

</div>

S tem smo za vsak $0 \leq i < n$ našli natanko določen $j$, da je $V_{i+1}/V_i \cong W_{j+1}/W_j$. Premislimo še, da je to prirejanje injektivno. Indeks $j$ je enolično določen s pogojem, da je $V_{i,j+1}/V_{i,j} \neq 0$, kar je po gornjem izomorfizmu enakovredno pogoju $W_{j,i+1}/W_{j,i} \neq 0$. Ker je $W_{j+1}/W_j$ nerazcepen, je slednji pogoj lahko izpolnjen le za *en* indeks $i$.

</div>

Iz izreka sledi, da lahko za vsako upodobitev $\rho$ grupe $G$ na končnorazsežnem prostoru najdemo bazo prostora, v kateri imajo vse matrike $\rho(g)$ za $g \in G$ *bločnozgornjetrikotno* obliko (pri čemer je število blokov enako dolžini kompozicijske vrste). Po drugi strani lahko za *polenostavno* upodobitev najdemo bazo prostora, v kateri imajo vse matrike *bločnodiagonalno* obliko.

### Izotipične komponente

Po zadnjem izreku je za dano upodobitev $\rho$ na končnorazsežnem prostoru in nerazcepno upodobitev $\pi$ število kompozicijskih faktorjev, ki so izomorfni $\pi$, neodvisno od kompozicijske vrste. Temu številu pravimo <span class="definicija">večkratnost</span> $\pi$ v $\rho$ in ga označimo z $\mult_{\rho}(\pi)$.

Kadar je dana upodobitev *polenostavna*, je do izomorfizma natančno enolično določena s svojimi večkratnostmi. Če je $\rho = \bigoplus_{i \in I} \rho_i$, potem je
```{math}
\hom_G(\pi, \rho) = \bigoplus_{i \in I} \hom_G(\pi, \rho_i).
```
Po Schurovi lemi je (nad algebraično zaprtim poljem) vsak od zadnjih prostorov spletičen bodisi trivialen bodisi enorazsežen. Večkratnost $\pi$ v $\rho$ lahko zatorej izračunamo kot
```{math}
\textstyle \mult_{\rho}(\pi) = \dim \hom_G(\pi, \rho).
```

<div class="zgled">

- Za eničnozgornjetrikotno upodobitev $\rho$ grupe $\RR$ na $\RR^2$ je $\mult_{\rho}(\oneone) = 2$. Ker ta upodobitev ni trivialna, ne more biti polenostavna, saj bi sicer bila izomorfna $\oneone^2$.

- Opazujmo permutacijsko upodobitev $\pi$ grupe $S_3$ na $\RR^3$. To upodobitev smo že razstavili na direktno vsoto $\oneone \oplus \rho$, kjer je $\rho$ dvorazsežna nerazcepna upodobitev na podprostoru $\langle u_1 = e_1 - e_2, u_2 = e_2 - e_3 \rangle$. Premislili smo, kako lahko to upodobitev projiciramo do upodobitve $\tilde \rho$ grupe $S_3$ na prostoru $(\ZZ/3\ZZ)^2$ nad končnim poljem $\ZZ/3\ZZ$.

  Upodobitev $\tilde \rho$ *ni* nerazcepna, saj ima invarianten podprostor $\langle u_1 - u_2 = e_1 + e_2 + e_3 \rangle$. Na tem podprostoru grupa $S_3$ deluje trivialno. V kvocientu $(\ZZ/3\ZZ)^2/\langle u_1 - u_2 \rangle \cong \ZZ/3\ZZ$ generatorja $(1\ 2)$ in $(1 \ 2 \ 3)$ grupe $S_3$ preslikata odsek vektorja $u_1$ v odsek $-u_1$ oziroma $u_1$. V tem prepoznamo predznačno upodobitev, interpretirano kot homomorfizem $\sgn \colon S_3 \to \GL_1(\ZZ/3\ZZ) \cong \{ 1, -1 \}$. Nad poljem $\ZZ/3\ZZ$ za permutacijsko upodobitev $\pi$ tako velja $\mult_{\pi}(\oneone) = 2$ in $\mult_{\pi}(\sgn) = 1$.

  Premislimo, da upodobitev $\pi$ nad $\ZZ/3\ZZ$ *ni* polenostavna. Če bi namreč bila, bi po zgornjem morala biti izomorfna direktni vsoti $\oneone \oplus \oneone \oplus \sgn$. Prostor $(\ZZ/3\ZZ)^3$ bi zatorej imel bazo, v kateri bi matriki za $\pi((1 \ 2))$ in $\pi((1 \ 2 \ 3))$ bili hkrati diagonalni. Ti dve matriki bi zato komutirali, kar pomeni, da bi morali komutirati tudi linearni preslikavi $\pi((1 \ 2))$ in $\pi((1 \ 2 \ 3))$. Temu pa ni tako, saj na primer velja $\pi((1 \ 2 \ 3)(1 \ 2)) e_1 = e_3$ in $\pi((1 \ 2)(1 \ 2 \ 3)) e_1 = e_1$.

</div>

Čeravno so kompozicijski faktorji upodobitve enolično določeni do permutacije natančno, pa *ni* res, da so enolično določeni tudi členi kompozicijske vrste, niti kadar je dana upodobitev polenostavna. Lahko se namreč zgodi, da neka nerazcepna podupodobitev nastopa z večkratnostjo vsaj $2$.[^7]

Oglejmo si tako situacijo še podrobneje. Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$. Naj bo $\pi$ neka *nerazcepna* upodobitev grupe $G$. Opazujmo vse $G$-invariantne podprostore v $V$, ki so kot upodobitve izomorfni $\pi$. Vsota (ne nujno direktna) vseh teh podprostorov
```{math}
\textstyle \Izotip_{\rho}(\pi) = \sum_{W \leq V, \ W \cong \pi} W
```
je <span class="definicija">$\pi$-izotipična komponenta</span> upodobitve $\rho$. Ta je sicer definirana za vsako upodobitev, a jo je za polenostavne upodobitve še posebej lahko določiti.

<div class="trditev">

Naj bo $G$ grupa s polenostavno upodobitvijo $\rho = \bigoplus_{i \in I} \rho_i$ na prostoru $V = \bigoplus_{i \in I} V_i$, kjer je vsak $\rho_i$ nerazcepna podupodobitev. Za vsako nerazcepno upodobitev $\pi$ grupe $G$ je
```{math}
\textstyle \Izotip_{\rho}(\pi) = \bigoplus_{i \in I \colon \ \rho_i \cong \pi} V_i.
```

</div>

<div class="dokaz">

Naj bo $W$ direktna vsota podprostorov $V_i$, ki so kot upodobitev izomorfni $\pi$. Seveda je $W \leq \Izotip_{\rho}(\pi)$. Dokažimo, da velja tudi obratna neenakost. Naj bo $U$ direktna vsota tistih prostorov $V_i$, ki kot upodobitev *niso* izomorfni $\pi$. Velja $V = W \oplus U$. Opazujmo projekcijo $p \colon V \to U$ z jedrom $W$. Naj bo $Z \leq \Izotip_{\rho}(\pi)$ podprostor, ki je kot upodobitev izomorfen $\pi$. Zožitev $p|_Z$ je spletična v $\hom_G(Z, U)$, ki je po Schurovi lemi ničeln prostor. Torej je $p(Z) = 0$ in s tem $Z \leq W$. Ker je bil $Z$ poljuben, smo s tem dokazali $\Izotip_{\rho}(\pi) \leq W$.

</div>

Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$ in nerazcepno upodobitvijo $\pi$ na prostoru $W$. Vsak $G$-invarianten podprostor v $V$, ki je kot upodobitev izomorfen $\pi$, lahko dobimo kot sliko prostora $W$ z neko spletično v $\hom_G(\pi, \rho)$.[^8] Vsoto vseh takih $G$-invariantnih podprostorov lahko torej zajamemo kot sliko linearne preslikave
```{math}
\Sigma_{\pi, \rho} \colon \hom_G(\pi, \rho) \otimes W \to V, \quad
    \Phi \otimes w \mapsto \Phi(w).
```
S tem je $\image \Sigma_{\pi, \rho} = \Izotip_{\rho}(\pi)$. Grupa $G$ deluje na $\hom_G(\pi, \rho) = \hom(W,V)^G$ trivialno, na $W$ pa prek $\pi$. Na ta način je $\Sigma_{\pi, \rho}$ celo spletična upodobitev.

<div class="trditev">

Naj bo $G$ grupa z upodobitvijo $\rho$ in nerazcepno upodobitvijo $\pi$ nad algebraično zaprtim poljem. Predpostavimo, da je $\dim \hom_G(\pi, \rho) < \infty$. Tedaj je $\Sigma_{\pi, \rho}$ injektivna.

</div>

<div class="dokaz">

Naj bo $\{ \Phi_i \}_{i \in I}$ baza prostora $\hom_G(\pi, \rho)$. Premislimo, da prostori $\image \Phi_i$ tvorijo notranjo direktno vsoto v $V$. Injektivnost $\Sigma_{\pi, \rho}$ od tod neposredno sledi.

Dokazujemo s protislovjem. Naj bo $J \subseteq I$ množica najmanjše moči, za katero prostori $\image \Phi_j$ za $j \in J$ *ne* tvorijo direktne vsote. Obstaja torej $k \in J$, da je
```{math}
\image \Phi_k \cap \sum_{j \in J \backslash \{ k \}} \image \Phi_j \neq 0.
```
Po nerazcepnosti $\pi$ je spletična $\Phi_k$ injektivna, zato je $\image \Phi_k$ nujno vsebovana v vsoti $\sum_{j \in J \backslash \{ k \}} \image \Phi_j$. Po minimalnosti $J$ je zadnja vsota direktna, zato je
```{math}
\Phi_k \in \hom_G(W, \bigoplus_{j \in J \backslash \{ k \}} \image \Phi_j).
```
Slednji prostor je direktna vsota prostorov $\hom_G(W, \image \Phi_j)$. Po Schurovi lemi je vsak od teh enorazsežen, zato je $\hom_G(W, \image \Phi_j)$ generiran s spletično $\Phi_j$. Od tod sledi, da je $\Phi_k$ linearna kombinacija spletičen $\Phi_j$ za $j \in J \backslash \{ k \}$. To je protislovno z dejstvom, da je $\{ \Phi_i \}_{i \in I}$ baza prostora $\hom_G(\pi, \rho)$.

</div>

<div class="posledica">

Naj bo $G$ grupa z upodobitvijo $\rho$ in nerazcepno upodobitvijo $\pi$ nad algebraično zaprtim poljem. Predpostavimo, da je $\hom_G(\pi, \rho) < \infty$. Izotipična komponenta $\Izotip_{\rho}(\pi)$ je polenostavna, $\pi$-izotipična in vsebuje $\pi$ z večkratnostjo $\dim \hom_G(\pi, \rho)$.

</div>

<div class="dokaz">

Iz injektivnosti $\Sigma_{\pi, \rho}$ sledi $\Izotip_{\rho}(\pi) \cong \hom_G(\pi, \rho) \otimes W$. Ker grupa $G$ deluje trivialno na $\hom_G(\pi, \rho)$, je prostor $\hom_G(\pi, \rho) \otimes W$ kot upodobitev izomorfen direktni vsoti $\dim \hom_G(\pi, \rho)$ kopij prostora $W$, na katerem $G$ deluje s $\pi$.

</div>

<div class="domacanaloga">

Naj bo $G$ grupa s končnorazsežno upodobitvijo $\rho$ na prostoru $V$ nad algebraično zaprtim poljem. Premisli, da se izotipične komponente, ki pripadajo paroma neizomorfnim nerazcepnim upodobitvam, sekajo trivialno.

</div>

<div class="zgled">

- Naj bo $G$ grupa s polenostavno upodobitvijo $\rho = \bigoplus_{i \in I} \rho_i$ na prostoru $V = \bigoplus_{i \in I} V_i$, v kateri vsaka nerazcepna podupodobitev nastopa z večkratnostjo $1$. Upodobitve $\rho_i$ so torej paroma neizomorfne. Izotipične komponente so torej kar enake podprostorom $V_i$. Ker so te komponente neodvisne od izbire dekompozicije, so torej podprostori $V_i$ polenostavne dekompozicije enolično določeni.

  Naj bo $W \leq V$ nek $G$-invarianten podprostor. Upodobitev $G$ na tem podprostoru je tudi polenostavna. Vsaka njena nerazcepna podupodobitev je hkrati podupodobitev $\rho$, zato po enoličnosti podprostorov $V_i$ sestoji iz nekaterih teh podprostorov. Prostor $W$ je zato enak $\bigoplus_{i \in J} V_i$ za neko podmnožico $J \subseteq I$.

  Za konkreten zgled lahko vzamemo ciklično grupo $\ZZ/n\ZZ$ in njeno regularno upodobitev, ki smo jo razcepili na direktno vsoto upodobitev $\bigoplus_{j \in \{ 1,2,\dots,n \}} \chi_j$. Po zadnjem komentarju je vsaka podupodobitev regularne upodobitve torej enaka direktni vsoti nekaterih od upodobitev $\chi_j$.

- Naj bo $G$ grupa z upodobitvijo $\rho$ na prostoru $V$ in naj bo $\pi$ neka njena enorazsežna upodobitev. Taka upodobitev je seveda nerazcepna. Vektor $v \in V$ pripada izotipični komponenti $\Izotip_{\rho}(\pi)$, če in samo če grupa $G$ na prostoru $\langle v \rangle$ deluje kot s $\pi$, se pravi
  ```{math}
  \textstyle \Izotip_{\rho}(\pi) = \left\{ v \in V \mid \forall g \in G \colon \ \rho(g) \cdot v = \pi(g) v \right\},
  ```
  pri čemer $\pi$ interpretiramo kot preslikavo v polje.

  Kadar je grupa $G$ abelova, je vsaka njena nerazcepna upodobitev nad algebraično zaprtim poljem enorazsežna. Vsaka polenostavna upodobitev take grupe je zato direktna vsota podprostorov, na katerih grupa deluje s skalarnimi množenji prek svojih enorazsežnih upodobitev.

</div>

## Matrični koeficienti

Vsaka upodobitev dane grupe je homomorfizem v grupo obrnljivih matrik $\GL(V)$. Do sedaj smo na upodobitve gledali z bolj konceptualnega stališča: govorili smo o strukturi prostora $V$ in o njegovi morebitni dekompoziciji na nerazcepne upodobitve. Zdaj si bomo z vsako od teh umazali roke in jo pogledali še podrobneje.

Predpostavimo, da je prostor $V$ končnorazsežen. Izberimo bazo prostora $V$ in s tem izomorfizem $V \cong F^n$ za nek $n$, tako da je upodobitev dana s homomorfizmom $\rho \colon G \to \GL_n(F)$. Vsak tak homomorfizem je *po komponentah* podan s svojimi <span class="definicija">matričnimi koeficienti</span>; to so funkcije
```{math}
f_{i,j} \colon G \to F, \quad
    g \mapsto \langle e_i^*, \rho(g) \cdot e_j \rangle = \rho(g)_{i,j}
```
za $i,j \in \{ 1, 2, \dots, n \}$.

O matričnih koeficientih upodobitve $\rho$ lahko abstraktneje govorimo tudi brez izbire baze prostora. Za vsak vektor $v \in V$ in kovektor $\lambda \in V^*$ definiramo $f_{v, \lambda} \colon G \to F$, $g \mapsto \langle \lambda, \rho(g) \cdot v \rangle$. To so <span class="definicija">posplošeni matrični koeficienti</span>. Kadar je prostor $V$ končnorazsežen, lahko vsak vektor razvijemo po izbrani bazi in vsak kovektor po dualni bazi, s čimer posplošeni matrični koeficient razvijemo po običajnih matričnih koeficientih.

### Matrični koeficienti in regularna upodobitev

Matrične koeficiente lahko vidimo kot elemente vektorskega prostora funkcij $\fun(G,F)$ iz $G$ v $F$. Na tem prostoru deluje grupa $G$ z regularno upodobitvijo $\rho_{\fun}$. Naj bo $\MK(\pi) \leq \fun(G,F)$ podprostor, ki ga razpenjajo matrični koeficienti neke končnorazsežne nerazcepne upodobitve $\pi$.[^9]

<div class="trditev">

$\MK(\pi)$ je $G$-invarianten podprostor.

</div>

<div class="dokaz">

Naj bo $g \in G$ in $f_{v, \lambda}$ posplošen matrični koeficient. Velja
```{math}
(g \cdot f_{v, \lambda}) \colon x \mapsto f_{v, \lambda}(xg) =
    \langle \lambda, \pi(xg) \cdot v \rangle =
    f_{\pi(g) \cdot v, \lambda}(x),
```
zato je $g \cdot f_{v, \lambda} = f_{\pi(g) \cdot v, \lambda} \in \MK(\pi)$.

</div>

Matrični koeficienti upodobitve $\pi$ nam torej dajejo podupodobitev na prostoru $\MK(\pi)$ znotraj regularne upodobitve $\rho_{\fun}$ na $\fun(G,F)$. Ni presenetljivo, da je ta podupodobitev v resnici tesno povezana s $\pi$.

<div class="izrek">

Naj bo $G$ grupa s končnorazsežno nerazcepno upodobitvijo $\pi$. Tedaj je
```{math}
\textstyle  \MK(\pi) = \Izotip_{\rho_{\fun}}(\pi)
```
Nad algebraično zaprtim poljem je večkratnost $\pi$ v slednji upodobitvi enaka $\deg(\pi)$.

</div>

<div class="dokaz">

Naj bo $\pi$ upodobitev na prostoru $W$. Spomnimo se, da je $\pi$-izotipična komponenta v $\rho_{\fun}$ napeta na vektorje oblike $\Phi(w)$ za $\Phi \in \hom_G(\pi, \rho_{\fun})$ in $w \in W$. Regularno upodobitev predstavimo kot inducirano upodobitev $\rho_{\fun} = \Ind^G_1(\oneone)$. Po adjunkciji med restrikcijo in indukcijo je
```{math}
\textstyle \hom_G(\pi, \rho_{\fun}) \cong \hom_1(\Res^G_1(\pi), \oneone)
    \cong \hom(\oneone^{\deg(\pi)}, \oneone).
```
Naj bo $\{ e_i \mid 1 \leq i \leq \deg(\pi) \}$ neka izbrana baza prostora $W$. Po zgornji adjunkciji s tem dobimo bazo
```{math}
\Phi_i \colon W \to \fun(G,F), \quad
    w \mapsto \left( g \mapsto \langle e_i^*, \pi(g) \cdot w \rangle \right) = f_{e_i^*, w}
```
prostora spletičen $\hom_G(\pi, \rho_{\fun})$ za $1 \leq i \leq \deg(\pi)$. Ko te bazne spletične evalviramo na izbrani bazi prostora $W$, dobimo torej ravno prostor $\MK(\pi)$. Nad algebraično zaprtim poljem te evalvacije tvorijo celo bazo[^10]
```{math}
\Phi_i(f_j) = f_{i,j}
```
prostora $\Izotip_{\rho_{\fun}}(\pi)$. V izbranih bazah torej matrični koeficienti tvorijo bazo za $\pi$-izotipično komponento regularne upodobitve. Večkratnost $\pi$ v njej je enaka $\dim \hom_G(\pi, \rho_{\fun}) = \deg(\pi)$.

</div>

Izpostavimo pomembno posledico, ki nam pove, da lahko vse nerazcepne upodobitve najdemo v regularni.

<div class="posledica">

Vsaka končnorazsežna nerazcepna upodobitev dane grupe je uresničljiva kot podupodobitev regularne.

</div>

V posebnem smo tekom zadnjega dokaza izpeljali, da so po izbiri baze matrični koeficienti končnorazsežne nerazcepne upodobitve nad algebraično zaprtim poljem $\pi$ vselej linearno neodvisni.[^11] Vseh je ravno $\deg(\pi)^2$ in znotraj regularne upodobitve tvorijo podupodobitev $\MK(\pi)$, ki sestoji iz $\deg(\pi)$ mnogo kopij upodobitve $\pi$.

Vse podobno velja, kadar imamo namesto ene same nerazcepne upodobitve *končno mnogo* paroma neizomorfnih nerazcepnih upodobitev $\{ \pi_i \}_{i \in I}$ dane grupe $G$. Vsaka od njih nam po izbiri baze podari svoje matrične koeficiente. Ti razpenjajo prostore, ki so enakim izotipičnim komponentam v regularni upodobitvi in te komponente tvorijo notranjo direktno vsoto. Matrični koeficienti vseh teh upodobitev so torej linearno neodvisni med sabo. Vseh skupaj je $\sum_{i \in I} \deg(\pi_i)^2$.

Matrični koeficienti so elementi prostora funkcij $\fun(G,F)$. V primeru, ko je grupa končna, lahko po primerjanju dimenzij zato izpeljemo neenakost
```{math}
\sum_{i \in I} \deg(\pi_i)^2 \leq \dim \fun(G,F) = |G|.
```

<div class="posledica">

Končna grupa ima le končno mnogo končnorazsežnih nerazcepnih upodobitev. Nad algebraično zaprtim poljem je vsaka od njih stopnje kvečjemu $\sqrt{|G|}$.

</div>

<div class="dokaz">

Vsaka končnorazsežna nerazcepna upodobitev je vsebovana v regularni in se zatorej pojavi kot njen kompozicijski faktor. Vseh možnih kompozicijskih faktorjev je končno mnogo, ker je prostor $\fun(G,F)$ končnorazsežen. Drugi del posledice sledi neposredno iz neenakosti pred njo.

</div>

<div class="zgled">

Opazujmo grupo $S_3$ nad poljem $\CC$. Njeno regularno upodobitev smo že razstavili na direktno vsoto $\oneone \oplus \rho$, kjer je $\rho$ dvorazsežna nerazcepna upodobitev. Poleg tega poznamo še enorazsežno predznačno upodobitev $\sgn$. Vsota kvadratov stopenj teh treh upodobitev je $1^2 + 1^2 + 2^2 = 6$, kar je ravno enako moči grupe $S_3$. Od tod sledi, da so te tri *vse* končnorazsežne nerazcepne upodobitve grupe $S_3$.

</div>

Več o upodobitvah končnih grup si bomo pogledali nekoliko kasneje.

### Karakterji

Naj bo $G$ grupa in $\rho$ njena končnorazsežna upodobitev. Po izbiri baze dobimo matrične koeficiente $f_{i,j}$. Te lahko kombiniramo na različne načine, da dobimo funkcije v $\fun(G,F)$, ki so nazadnje *neodvisne* od izbire baze. Najosnovnejša[^12] taka funkcija je sled linearnega operatorja, se pravi
```{math}
\textstyle \chi_{\rho} \colon G \to F, \quad
    g \mapsto \tr(\rho(g)) = \sum_{i = 1}^{\deg(\rho)} f_{i,i}(g).
```
To funkcijo imenujemo <span class="definicija">karakter</span> upodobitve $\rho$. Kadar je upodobitev $\rho$ nerazcepna, tudi njenemu karakterju dodamo pridevnik *nerazcepen*.

Karakter je neodvisen od izbire baze, zato za vsaka $x, g \in G$ velja $\chi_{\rho}(x g x^{-1}) = \chi_{\rho}(g)$. Karakterji so torej funkcije na $G$, ki so konstantne na konjugiranostnih razredih.[^13] Takim funkcijam pravimo <span class="definicija">razredne funkcije</span> in jih označimo s
```{math}
\fun_{\cl}(G,F) = \{ f \in \fun(G,F) \mid \forall x, g \in G \colon f(x g x^{-1}) = f(g) \}.
```
Za dan konjugiranostni razred $\conclass$ v grupi $G$ bomo pisali $\chi_{\rho}(\conclass)$ za vrednost karakterja v poljubnem predstavniku tega razreda.

<div class="zgled">

Opazujmo grupo $S_3$ nad poljem $\CC$. Poznamo že vse tri njene končnorazsežne nerazcepne upodobitve. Določimo karakterje teh nerazcepnih upodobitev. Karakterji enorazsežnih upodobitev so kot funkcije kar enaki upodobitvam. Za karakter $\chi_{\rho}$ velja
```{math}
() \mapsto \tr \begin{pmatrix}
        1 & 0 \\ 0 & 1
    \end{pmatrix} = 2, \quad
    (1 \ 2) \mapsto \tr \begin{pmatrix}
        -1 & 1 \\ 0 & 1
    \end{pmatrix} = 0, \quad
    (1 \ 2 \ 3) \mapsto \tr \begin{pmatrix}
        0 & -1 \\ 1 & -1
    \end{pmatrix} = -1.
```
V grupi $S_3$ je vsak element konjugiran enemu od $()$, $(1 \ 2)$ ali $(1 \ 2 \ 3)$. S tem so torej vse vrednosti karakterja $\chi_{\rho}$ določene.

Vse podatke o vrednostih karakterjev dane grupe ponavadi zložimo v <span class="definicija">tabelo karakterjev</span>. Stolpce indeksiramo s predstavniki konjugiranostnih razredov, vrstice pa z nerazcepnimi karakterji. Vrednosti v tabeli so vrednosti karakterjev v konjugiranostnih razredih.

|                    | $()$ | $(1 \ 2)$ | $(1 \ 2 \ 3)$ |
|:------------------:|:------:|:-----------:|:---------------:|
| $\chi_{\oneone}$ | $1$  |    $1$    |      $1$      |
|  $\chi_{\sgn}$   | $1$  |   $-1$    |      $1$      |
|  $\chi_{\rho}$   | $2$  |    $0$    |     $-1$      |

Tabela karakterjev $S_3$

</div>

Že samo imenovanje karakterjev odzvanja, da to niso poljubne funkcije v $\fun(G,F)$, temveč da v nekem smislu zajemajo srž upodobitve.

<div class="trditev">

Naj bo $G$ grupa s končnorazsežnima nerazcepnima upodobitvama nad algebraično zaprtim poljem. Ti dve upodobitvi sta izomorfni, če in samo če imata enaka karakterja.

</div>

<div class="dokaz">

Ker so matrični koeficienti različnih nerazcepnih upodobitev linearno neodvisni med sabo, so tudi njihovi karakterji linearno neodvisni kot elementi prostora $\fun(G,F)$.

</div>

Karakterjev fundamentalnih konstrukcij različnih upodobitev ni težko izračunati.

<div class="trditev">

Naj bo $G$ grupa s končnorazsežnimi upodobitvami $\rho$, $\rho_1$, $\rho_2$. Tedaj za vse $g \in G$ velja
```{math}
\chi_{\rho}(1) = \deg(\rho), \quad
    \chi_{\rho_1 \oplus \rho_2} = \chi_{\rho_1} + \chi_{\rho_2}, \quad
    \chi_{\rho_1 \otimes \rho_2} = \chi_{\rho_1} \cdot \chi_{\rho_2}, \quad
    \chi_{\rho^*}(g) = \chi_{\rho}(g^{-1}).
```
Za podgrupo $H \leq G$ in poljuben $h \in H$ velja
```{math}
\chi_{\Res^G_H(\rho)}(h) = \chi_{\rho}(h).
```
Kadar je $H \leq G$ končnega indeksa in $\rho$ upodobitev grupe $H$, za poljubno izbiro predstavnikov desnih odsekov $R$ grupe $H$ v $G$ velja
```{math}
\chi_{\Ind^G_H(\rho)}(g) = \sum_{r \in R \colon r g r^{-1} \in H} \chi_{\rho}(r g r^{-1}).
```

</div>

<div class="dokaz">

Netrivialna je le zadnja enakost o indukciji. Naj $H$ deluje na prostoru $V$ prek $\rho$. Spomnimo se, da lahko induciran prostor identificiramo z direktno vsoto $\bigoplus_{r \in R} V r$, kjer je $Vr$ kopija prostora $V$ pri komponenti $r$. Element $g \in G$ deluje na $v r_0 \in V r_0$ kot
```{math}
g \cdot v r_0 = \left( \rho(h) \cdot v \right) r,
```
kjer je $r = h r_0 g^{-1}$ za enolično določena $r \in R$, $h \in H$. Prostori $V r$ se torej pri delovanju med sabo permutirajo, poleg tega pa grupa deluje netrivialno še na vsaki komponenti posebej. Za izračun sledi so zato relevantne samo komponente, ki so fiksne pri tej permutaciji. To so komponente $Vr_0$, za katere je $r = r_0$, se pravi komponente z lastnostjo $H r_0 g^{-1} = H r_0$, kar je nazadnje enakovredno pogoju $r_0 g r_0^{-1} \in H$. Za tako komponento $V r_0$ element $g$ deluje na vektorju $v r_0$ kot
```{math}
g \cdot v r_0 = \left( \rho(r_0 g r_0^{-1}) \cdot v \right) r_0,
```
zato je sled induciranega delovanja $g$ na $V r_0$ enaka $\chi_{\rho}(r_0 g r_0^{-1})$. Ko seštejemo prispevke po vseh relevantnih predstavnikih $r_0 \in R$, dobimo želeno formulo za induciran karakter.

</div>

<div class="zgled">

Naj bo $G$ končna grupa. V tem primeru je regularna upodobitev $\rho_{\fun}$ končnorazsežna. Določimo njen karakter najprej na roke. V regularni upodobitvi imamo naravno bazo iz karakterističnih funkcij
```{math}
1_{x} \colon G \to F, \quad
        y \mapsto \begin{cases} 1 & y = x, \\ 0 & \text{sicer.} \end{cases}
```
Na vsaki od teh element grupe $g \in G$ deluje kot $\rho_{\fun}(g) \cdot 1_x = 1_{x g^{-1}}$. Grupa $G$ torej permutira karakteristične funkcije. Sled preslikave $\rho_{\fun}(g)$ je zato enaka številu karakterističnih funkcij, ki jih ta preslikava fiksira. To je mogoče le, če je $x = x g^{-1}$, kar pa se zgodi zgolj pri $g = 1$, ko je $\rho_{\fun}(1) = \id$ s sledjo $\dim \fun(G,F) = |G|$. Torej je karakter regularne upodobitve končne grupe enak
```{math}
\chi_{\rho_{\fun}} \colon G \to F, \quad
        g \mapsto \begin{cases} |G| & g = 1, \\ 0 & \text{sicer.} \end{cases}
```

Ta karakter bi lahko hitreje izračunali s pomočjo znane identifikacije $\rho_{\fun} \cong \Ind^G_1(\oneone)$. V tem primeru je $R = G$ in za $g \neq 1$ je vsota v formuli za induciran karakter prazna, torej se evalvira v $0$, za $g = 1$ pa dobimo $\sum_{r \in G} \chi_{\oneone}(1) = |G|$.

</div>

Lastnost karakterjev kot srža upodobitve se prenese na končnorazsežne polenostavne upodobitve, *če je le polje ničelne karakteristike*. Karakter dane polenostavne upodobitve $\rho$ namreč lahko razvijemo kot
```{math}
\textstyle \chi_{\rho} = \sum_{\pi \in \Irr(G)} \mult_{\rho}(\pi) \cdot \chi_{\pi}.
```
Polenostavna upodobitev je enolično določena s svojimi nerazcepnimi komponentami in njihovimi večkratnostmi. Če je torej $\chi_{\rho_1} = \chi_{\rho_2}$ za polenostavni upodobitvi $\rho_1$, $\rho_2$, potem od tod iz neodvisnosti nerazcepnih karakterjev sledi enakost $\mult_{\rho_1}(\pi) = \mult_{\rho_2}(\pi)$ za vsako nerazcepno upodobitev $\pi$. To je enakost v polju $F$, od koder po predpostavki o ničelni karakteristiki sledi, da ta enakost velja tudi v kolobarju celih števil. S tem je $\rho_1 \cong \rho_2$.

<div class="posledica">

Nad algebraično zaprtim poljem ničelne karakteristike je polenostavna upodobitev do izomorfizma natančno določena s svojim karakterjem.

</div>

Karakterji so torej funkcije na grupi, s katerimi so v mnogih primerih upodobitve, ki so sicer mnogo bolj kompleksni objekti kot le funkcije na grupi, natančno določene. V nadaljevanju bomo videli, da lahko včasih eksplicitno izračunamo vse nerazcepne karakterje, brez da bi sploh poznali same nerazcepne upodobitve. Na ta način lahko dodobra razumemo kategorijo upodobitev dane grupe zgolj z uporabo karakterjev.

[^1]: Rečemo tudi, da je $V$ <span class="definicija">enostavna</span> upodobitev. Te terminologija izhaja iz alternativne obravnave upodobitev kot *modulov nad grupnimi algebrami*.

[^2]: Po analogiji s faktorizacijo števil si nerazcepne upodobitve lahko predstavljamo kot praštevila.

[^3]: Če komplementarna podupodobitev obstaja, potem je enolično določena (do izomorfizma upodobitev), saj je izomorfna kvocientu $\rho/\tilde\rho$.

[^4]: Linearna preslikava $A \colon X \to X$ je projekcija na podprostor $Y \leq X$, če je $A^2 = A$ in $\image A = Y$. Projekcijska spletična je torej spletična, ki je hkrati projekcija na nek podprostor.

[^5]: V nadaljevanju bomo pokazali, da so upodobitve *končnih* grup nad poljem karakteristike $0$ vselej poenostavne.

[^6]: Ta argument je soroden premisleku o obstoju Hirschove dolžine v policikličnih grupah iz [Teorije grup](https://urbanjezernik.github.io/teorija-grup/).

[^7]: Na primer, kadar je upodobitev trivialna, se pravi $V = \oneone^k$ za nek $k > 1$, lahko izberemo poljubno bazo prostora $V$ in prek nje dobimo nek drug izomorfizem $V \cong \oneone^k$.

[^8]: Vsaka neničelna spletična v $\hom_G(\pi, \rho)$ je namreč injektivna.

[^9]: Prostor $\MK(\pi)$ je enak prostoru, ki ga razpenjajo posplošeni matrični koeficienti upodobitve $\pi$, zato je neodvisen od izbire baze.

[^10]: Preslikava $\Sigma_{\pi, \rho_{\fun}}$ je injektivna, ker je $\dim \hom_G(\pi, \rho_{\fun}) = \deg(\pi) < \infty$.

[^11]: Temu dejstvu včasih pravimo *Burnsideov izrek o nerazcepnosti*.

[^12]: V resnici je sled do skalarja natančno *edina* taka funkcija.

[^13]: <span class="definicija">Konjugiranostni razred</span> elementa $g \in G$ je množica $\{ x g x^{-1} \mid x \in G \}$. Grupa $G$ je disjunktna unija konjugiranostnih razredov svojih elementov. Včasih uporabljamo oznako $g^x = x^{-1} g x$ in s tem oznako $g^G$ za konjugiranostni razred elementa $g$ v $G$.
