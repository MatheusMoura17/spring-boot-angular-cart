from bs4 import BeautifulSoup
import random
import json

# O dataset fornecido
dataset = """
<h3>1. Abacate (<em>Persea americana</em>)</h3>
<figure class="image"><img alt="abacate" height="476"
    src="https://static.todamateria.com.br/upload/ab/ac/abacate-cke.jpg" width="630">
  <figcaption>Abacate</figcaption>
</figure>
<p>Origin&aacute;rio da Am&eacute;rica Central, o abacate possui vitaminas A, B, C, D, E, prote&iacute;nas,
  c&aacute;lcio, magn&eacute;sio, f&oacute;sforo, ferro e pot&aacute;ssio. O Brasil &eacute;, provavelmente, o
  &uacute;nico lugar do mundo que o consome como sobremesa, utilizando a&ccedil;&uacute;car e leite. Em outros
  pa&iacute;ses, &eacute; usado como um alimento temperado com sal e azeite.</p>
<h3>2. Abacaxi (<em>Ananas comosus</em>)</h3>
<figure class="image"><img alt="abacaxi" height="516"
    src="https://static.todamateria.com.br/upload/ab/ac/abacaxi-0-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ab/ac/abacaxi-0-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Abacaxi</figcaption>
</figure>
<p>Encontrado originalmente em toda a Am&eacute;rica do Sul tropical, o abacaxi &eacute; rico em vitamina C e contribui
  para o funcionamento do sistema imunol&oacute;gico. Tamb&eacute;m auxilia na perda de peso e al&iacute;vio das dores
  musculares.</p>
<h3>3. A&ccedil;a&iacute; (<em>Euterpe oleracea</em>)</h3>
<figure class="image"><img alt="a&ccedil;a&iacute;" height="418"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta3-0-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta3-0-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>A&ccedil;a&iacute;</figcaption>
</figure>
<p>Uma das frutas brasileiras mais conhecidas em todo o mundo e t&iacute;pica da Amaz&ocirc;nia. O a&ccedil;a&iacute;
  &eacute; um alimento altamente energ&eacute;tico, rico em c&aacute;lcio, sais minerais, f&oacute;sforo e ferro. Pode
  ser consumido a partir da prepara&ccedil;&atilde;o do seu vinho ou suco e tamb&eacute;m associado com granola, mel e
  outras frutas, ou ainda em pratos salgados.</p>
<h3>4. Acerola (<em>Malpighia emarginata</em>)</h3>
<figure class="image"><img alt="acerola" height="419"
    src="https://static.todamateria.com.br/upload/ac/er/acerola-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ac/er/acerola-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Acerola</figcaption>
</figure>
<p>Origin&aacute;ria da Am&eacute;rica Central, a acerola &eacute; fonte de vitamina C e auxilia no combate a
  doen&ccedil;as respirat&oacute;rias. &Eacute; consumida natural ou ainda como suco, doces, geleias e sorvetes.</p>
<h3>5. Amora (<em>Morus alba</em>)</h3>
<figure class="image"><img alt="amora" height="411"
    src="https://static.todamateria.com.br/upload/am/or/amora-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/am/or/amora-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Amora</figcaption>
</figure>
<p>A amora &eacute; uma fruta rica em vitaminas A, C e K e possui propriedades anti-inflamat&oacute;rias. Ela contribui
  para combater a anemia e o envelhecimento. Seu consumo pode ser in natura ou ainda utilizada no preparo de sobremesas
  ou sucos.</p>
<h3>6. Araticum (<em>Annona coriacea</em>)</h3>
<figure class="image"><img alt="araticum" height="419"
    src="https://static.todamateria.com.br/upload/ar/at/araticummelhorar.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ar/at/araticummelhorar.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Araticum</figcaption>
</figure>
<p>O Araticum &eacute; uma fruta t&iacute;pica do Cerrado brasileiro. Ela possui ferro, pot&aacute;ssio, c&aacute;lcio,
  vitaminas C, A, B1 e B2 e tem peso m&eacute;dio de 2 kg. O araticum ainda possui antioxidantes que auxiliam na
  preven&ccedil;&atilde;o de doen&ccedil;as degenerativas. Apresenta aroma forte, polpa doce e amarelada, sendo
  consumida in natura ou em forma de doces, sucos, iogurte, geleias e sorvetes.</p>
<h3>7. Bacaba (<em>Oenocarpus bacaba</em>)</h3>
<figure class="image"><img alt="bacaba" height="388"
    src="https://static.todamateria.com.br/upload/ba/ca/bacaba-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ba/ca/bacaba-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Bacaba</figcaption>
</figure>
<p>Nativa da Amaz&ocirc;nia, a partir desta fruta prepara-se o vinho que pode ser consumido com farinha de mandioca e
  a&ccedil;&uacute;car. O &oacute;leo de bacaba &eacute; tamb&eacute;m muito utilizado na pele, especialmente por agir
  de forma nutritiva e revitalizante. &Eacute; uma fruta rica em prote&iacute;nas e carboidratos, sendo recomendada para
  atletas.</p>
<h3>8. Banana (<em>Musa sp.</em>)</h3>
<figure class="image"><img alt="banana" height="353"
    src="https://static.todamateria.com.br/upload/ba/na/banana-0-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ba/na/banana-0-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Banana</figcaption>
</figure>
<p>Rica em minerais e vitaminas que auxiliam no sistema imunol&oacute;gico, a <a href="/banana/">banana</a> podem ser
  consumida fresca, cozida, frita, assada ou desidratada. Importante lembrar que existe uma grande variedade de bananas
  no mundo, no Brasil as mais conhecidas s&atilde;o: nanica, ouro, ma&ccedil;&atilde;, prata e da terra.</p>
<h3>9. Birib&aacute; (<em>Rollinia mucosa</em>)</h3>
<figure class="image"><img alt="birib&aacute;" height="472"
    src="https://static.todamateria.com.br/upload/bi/ri/biriba-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/bi/ri/biriba-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Birib&aacute;</figcaption>
</figure>
<p>T&iacute;pica da Amaz&ocirc;nia, o birib&aacute; &eacute; uma fruta de sabor suave e adocicado, sendo muito consumida
  em estado natural. Tamb&eacute;m &eacute; utilizada para prepara&ccedil;&atilde;o de sucos e sorvetes. O consumo do
  birib&aacute; auxilia no funcionamento intestinal e fortalece o sistema imunol&oacute;gico. &Eacute; rica em vitamina
  C e pot&aacute;ssio, al&eacute;m de apresentar prote&iacute;nas, lip&iacute;deos, fibras e sais minerais.</p>
<h3>10. Cacau (<em>Theobroma cacao</em>)</h3>
<figure class="image"><img alt="cacau" height="330"
    src="https://static.todamateria.com.br/upload/ca/ca/cacau-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ca/ca/cacau-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Cacau</figcaption>
</figure>
<p>De origem brasileira, da regi&atilde;o Amaz&ocirc;nica, o cacau &eacute; a mat&eacute;ria-prima do chocolate. Essa
  fruta &eacute; rica em fibras e minerais, como ferro, f&oacute;sforo e c&aacute;lcio. Tamb&eacute;m pode ser consumida
  como suco.</p>
<div id="todamateria_inarticle_mrec1" class="ad-unit ad-unit--pt-br"><amp-ad width="336" height="280" type="doubleclick"
    data-slot="/1062898/todamateria_inarticle_mrec1" data-multi-size="300x250,250x250,200x200"
    data-enable-refresh="30"></amp-ad></div>
<h3>11. Caj&aacute; (<em>Spondias mombin</em>)</h3>
<figure class="image"><img alt="caj&aacute;" height="420"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta11-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta11-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Caj&aacute;</figcaption>
</figure>
<p>O caj&aacute; &eacute; uma fruta rica em sais minerais. Com um sabor agridoce e uma polpa suculenta, ela auxilia no
  cansa&ccedil;o mental, estresse, ins&ocirc;nia e inflama&ccedil;&otilde;es na garganta. &Eacute; rica em fibras que
  auxiliam no funcionamento do intestino, em vitaminas C e minerais que fortalecem os ossos.</p>
<h3>12. Caqui (<em>Diospyros kaki</em>)</h3>
<figure class="image"><img alt="caqui" height="374"
    src="https://static.todamateria.com.br/upload/ca/qu/caqui-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ca/qu/caqui-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Caqui</figcaption>
</figure>
<p>Origin&aacute;rio da China, o caqui possui vitaminas A, B1, B2 e E, al&eacute;m de c&aacute;lcio, ferro e
  prote&iacute;nas. Essa fruta tem a apar&ecirc;ncia muito semelhante a de um tomate. Pode ser consumida in natura, ou
  ainda em preparos de sobremesas, geleias e sorvete.</p>
<h3>13. Carambola (<em>Averrhoa carambola</em>)</h3>
<figure class="image"><img alt="carambola" height="420"
    src="https://static.todamateria.com.br/upload/ca/ra/carambola-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ca/ra/carambola-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Carambola</figcaption>
</figure>
<p>Origin&aacute;ria do Sudeste da &Aacute;sia, a carambola cont&eacute;m vitaminas A, B e C. Ela auxilia o sistema
  imunol&oacute;gico na defesa do organismo e ajuda a reduzir a taxa de glicose no sangue. Apresenta sabor agridoce,
  podendo ser utilizada em preparos doces e na composi&ccedil;&atilde;o de saladas.</p>
<h3>14. Cereja (<em>Prunus avium</em>)</h3>
<figure class="image"><img alt="cereja" height="345"
    src="https://static.todamateria.com.br/upload/ce/re/cereja-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ce/re/cereja-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Legenda</figcaption>
</figure>
<p>Origin&aacute;ria da &Aacute;sia, a cereja &eacute; uma fruta rica em vitaminas A, B e C, c&aacute;lcio,
  f&oacute;sforo, ferro e vitaminas. Ela contribui para a redu&ccedil;&atilde;o do reumatismo, gota, artrite e dores
  musculares. Seu consumo pode ser in natura ou no preparo de compostas.</p>
<h3>15. Cidra (<em>Citrus medica</em>)</h3>
<figure class="image"><img alt="cidra" height="472"
    src="https://static.todamateria.com.br/upload/ci/dr/cidra-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ci/dr/cidra-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Cidra</figcaption>
</figure>
<p>A cidra assemelha-se a um lim&atilde;o gigante sem forma regular e pode pesar at&eacute; 5 kg. Possui as vitaminas A,
  B1, B2, B5 e C, al&eacute;m de ferro, f&oacute;sforo e c&aacute;lcio. &Eacute; uma fruta que cont&eacute;m grande
  concentra&ccedil;&atilde;o de &aacute;cido c&iacute;trico. &Eacute; muito utilizada para compotas doces.</p>
<h3>16. Coco (<em>Cocos nucifera L.</em>)</h3>
<figure class="image"><img alt="coco" height="418"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta16-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta16-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Coco verde e coco seco</figcaption>
</figure>
<p>O coco &eacute; uma fruta rica em gorduras boas, sais minerais e fibras. Sua polpa &eacute; branca e o interior com
  &aacute;gua. Ele pode ser consumido quando verde ou maduro. O coco possui duas partes comest&iacute;veis, o fruto e a
  &aacute;gua. Quando o coco est&aacute; verde sua polpa apresenta consist&ecirc;ncia mole, sendo consumido de colher.
  J&aacute; quando est&aacute; maduro (seco) &eacute; poss&iacute;vel consumir em peda&ccedil;os ou utilizar para
  extra&ccedil;&atilde;o de leite e &oacute;leo.</p>
<h3>17. Cupua&ccedil;u (<em>Theobroma grandiflorum</em>)</h3>
<figure class="image"><img alt="cupua&ccedil;&uacute;" height="420"
    src="https://static.todamateria.com.br/upload/cu/pu/cupuacu-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/cu/pu/cupuacu-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Cupua&ccedil;u</figcaption>
</figure>
<p>T&iacute;pica da Amaz&ocirc;nia, seu uso mais comum &eacute; em forma de cremes, sorvetes e sucos. De suas sementes
  &eacute; poss&iacute;vel a fabrica&ccedil;&atilde;o de chocolate e doces. O consumo do cupua&ccedil;u &eacute;
  indicado como fonte de energia. Possui &aacute;cidos graxos que auxiliam na diminui&ccedil;&atilde;o do colesterol,
  al&eacute;m de vitamina A e C, vitaminas B1, B2 e B3, fibras e sais minerais como c&aacute;lcio, f&oacute;sforo e
  sel&ecirc;nio.</p>
<h3>18. Figo (<em>Ficus carica L.</em>)</h3>
<figure class="image"><img alt="figo" height="630"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta18-0-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta18-0-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Figo roxo</figcaption>
</figure>
<p>O figo &eacute; uma fruta que possui alto &iacute;ndice de a&ccedil;&uacute;car, pot&aacute;ssio, c&aacute;lcio e
  f&oacute;sforo. Rico em fibras, ele auxilia na redu&ccedil;&atilde;o do colesterol sangu&iacute;neo. Tamb&eacute;m
  combate as infec&ccedil;&otilde;es respirat&oacute;rias e inflama&ccedil;&otilde;es devido &agrave;s suas
  propriedades. Geralmente &eacute; consumido fresco ou em compotas e geleias.</p>
<h3>19. Framboesa (<em>Rubus idaeus</em>)</h3>
<figure class="image"><img alt="framboesa" height="321"
    src="https://static.todamateria.com.br/upload/fr/am/framboesa-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/am/framboesa-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Framboesa</figcaption>
</figure>
<p>Origin&aacute;ria da Europa e parte da &Aacute;sia, a framboesa &eacute; fonte de vitaminas, c&aacute;lcio,
  f&oacute;sforo e ferro. Essa fruta atua contra o envelhecimento celular e previne algumas doen&ccedil;as. Pode ser
  consumida in natura, na forma de ch&aacute; e sucos.</p>



<h3>20. Goiaba (<em>Psidium guayava</em>)</h3>
<figure class="image"><img alt="goiaba" height="419"
    src="https://static.todamateria.com.br/upload/go/ai/goaiaba-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/go/ai/goaiaba-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Goiaba vermelha</figcaption>
</figure>
<p>Nativa da Am&eacute;rica Central, a goiaba &eacute; uma fruta bastante cultivada e apreciada no Brasil. Rica em
  vitamina C, ela possui vitaminas A, E e quase todas do complexo B, al&eacute;m de minerais, em menor quantidade. A
  goiaba &eacute; muito utilizada na fabrica&ccedil;&atilde;o de doces, sendo que a mais conhecida &eacute; a goiabada.
</p>
<h3>21. Groselha (<em>Ribes rubrum</em>)</h3>
<figure class="image"><img alt="groselha" height="414"
    src="https://static.todamateria.com.br/upload/gr/os/groselha-0-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/gr/os/groselha-0-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Groselha</figcaption>
</figure>
<p>Origin&aacute;ria da Europa e &Aacute;sia, a groselha &eacute; rica em vitamina C e pot&aacute;ssio. Possui
  tamb&eacute;m c&aacute;lcio, f&oacute;sforo, ferro, enxofre, magn&eacute;sio e prote&iacute;nas. A fruta atua na
  preven&ccedil;&atilde;o contra o c&acirc;ncer, envelhecimento, inflama&ccedil;&atilde;o e doen&ccedil;as
  neurol&oacute;gicas. A groselha &eacute; utilizada para fazer sucos.</p>
<div id="div-gpt-sg-96c63ecfe9c5cfec44384c5073cc79cd" class="ad-unit ad-unit--pt-br"><amp-ad width="336" height="280"
    type="doubleclick" data-slot="/1062898/todamateria_inarticle_mrec2" data-multi-size="300x250,250x250,200x200"
    data-enable-refresh="30"></amp-ad></div>
<h3>22. Ing&aacute; (<em>Inga edulis</em>)</h3>
<figure class="image"><img alt="ing&aacute;" height="430"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta22-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta22-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Ing&aacute;</figcaption>
</figure>
<p>Origin&aacute;ria da Amaz&ocirc;nia, a polpa da fruta envolve a semente, sendo consumida em estado natural. O
  ing&aacute; apresenta uma polpa branca e adocicada e &eacute; rica em sais minerais. Pode ser utilizado ainda como
  ch&aacute; para cicatrizante e como xarope no tratamento de bronquite.</p>
<h3>23. Jabuticaba (<em>Myrciaria cauliflora</em>)</h3>
<figure class="image"><img alt="Jabuticaba" height="630"
    src="https://static.todamateria.com.br/upload/ja/bu/jabuticaba-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ja/bu/jabuticaba-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Jabuticaba</figcaption>
</figure>
<p>A jabuticaba &eacute; uma fruta com casca cor roxa escura ou preta e interior branco. Com uma polpa suculenta, ela
  &eacute; rica em vitaminas do complexo B. A utiliza&ccedil;&atilde;o da casca da jabuticaba &eacute; muito comum em
  ch&aacute;s, que auxiliam na redu&ccedil;&atilde;o e combate de inflama&ccedil;&otilde;es e envelhecimento da pele.
  Pode ser consumida in natura, sorvete, geleias e licores.</p>
<h3>24. Jaca (<em>Artocarpus heterophyllus</em>)</h3>
<figure class="image"><img alt="jaca" height="381"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta24-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta24-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Jaca</figcaption>
</figure>
<p>Nativa da &Aacute;sia, a jaca possui c&aacute;lcio, pot&aacute;ssio, ferro, f&oacute;sforo e vitaminas A, B e C. Essa
  fruta pode pesar at&eacute; 15 kg. Seu consumo auxilia no combate a press&atilde;o alta e preven&ccedil;&atilde;o de
  doen&ccedil;as cardiovasculares. A alta quantidade de fibras favorece a digest&atilde;o e contribui com transtornos
  digestivos.</p>
<h3>25. Jambo (<em>Syzygium jambos</em>)</h3>
<figure class="image"><img alt="jambo" height="329"
    src="https://static.todamateria.com.br/upload/ja/mb/jambo-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ja/mb/jambo-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Jambo</figcaption>
</figure>
<p>Origin&aacute;rio da &Aacute;sia, o jambo possui ferro, f&oacute;sforo, prote&iacute;nas, carboidratos e vitamina A,
  B1 e B2. Possui baixo valor cal&oacute;rico e fortalece o sistema imunol&oacute;gico. Com um gosto refrescante, ele
  &eacute; consumido de forma natural.</p>
<h3>26. Jenipapo (<em>Genipa americana L.</em>)</h3>
<figure class="image"><img alt="jenipapo" height="630"
    src="https://static.todamateria.com.br/upload/je/ni/jenipapo-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/je/ni/jenipapo-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Jenipapo</figcaption>
</figure>
<p>O jenipapo &eacute; uma fruta que tem alta concentra&ccedil;&atilde;o de ferro e c&aacute;lcio. Apresenta suco de cor
  forte, que era utilizada pelos &iacute;ndios para pintar o corpo. Possui polpa suculenta, de aroma forte e sabor
  &aacute;cido e doce. A fruta &eacute; indicada para inflama&ccedil;&otilde;es intestinais, anemia e asma.</p>
<h3>27. Kiwi (<em>Actinidia deliciosa</em>)</h3>
<figure class="image"><img alt="kiwi" height="325"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta27kiwi-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta27kiwi-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Kiwi</figcaption>
</figure>
<p>O kiwi &eacute; uma fruta rica em fibras e vitaminas. Considerado um alimento importante contra o c&acirc;ncer e
  prote&ccedil;&atilde;o do DNA, a sua casca tamb&eacute;m pode ser consumida.</p>
<h3>28. Laranja (<em>Citrus sinensis</em>)</h3>



<figure class="image"><img alt="laranja" height="402"
    src="https://static.todamateria.com.br/upload/la/ra/laranja-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/la/ra/laranja-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Laranja</figcaption>
</figure>
<p>Rica em vitamina C, a laranja &eacute; uma fruta rica em &aacute;cido c&iacute;trico. Indicada para prevenir
  c&acirc;ncer, ela fortalece o sistema imunol&oacute;gico, reduz o colesterol e protege o cora&ccedil;&atilde;o. A
  laranja &eacute; consumida in natura, em forma de sucos e no preparo de sobremesas.</p>
<h3>29. Lim&atilde;o (<em>Citrus limon</em>)</h3>
<figure class="image"><img alt="lim&atilde;o" height="504"
    src="https://static.todamateria.com.br/upload/li/ma/limao-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/li/ma/limao-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Lim&atilde;o</figcaption>
</figure>
<p>Origin&aacute;rio da &Aacute;sia, o lim&atilde;o &eacute; fonte de vitamina C e minerais. Ele contribui na melhoria
  da digest&atilde;o, fortalece o sistema imunol&oacute;gico, ajuda a manter o peso e evita o envelhecimento precoce.
  &Eacute; consumido como tempero de pratos salgados e tamb&eacute;m no preparo de sucos e sobremesas.</p>
<h3>30. Ma&ccedil;&atilde; (<em>Malus domestica</em>)</h3>
<figure class="image"><img alt="ma&ccedil;&atilde;" height="319"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta30maca-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta30maca-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Diferentes tipos de ma&ccedil;&atilde;</figcaption>
</figure>
<p>Origin&aacute;ria da &Aacute;sia e Europa, a ma&ccedil;&atilde; &eacute; uma fruta que auxilia na
  preven&ccedil;&atilde;o de doen&ccedil;as. Possui vitaminas A, B1, B2, C e K, ferro e f&oacute;sforo. Apresenta
  subst&acirc;ncias e nutrientes que auxiliam no sistema imunol&oacute;gico.</p>
<h3>31. Mam&atilde;o (<em>Carica papaya</em>)</h3>
<figure class="image"><img alt="mam&atilde;o" height="625"
    src="https://static.todamateria.com.br/upload/ma/ma/mamao-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ma/ma/mamao-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Mam&atilde;o</figcaption>
</figure>
<p>O mam&atilde;o &eacute; uma fruta rica em vitaminas e minerais, como vitaminas C e E, c&aacute;lcio, f&oacute;sforo,
  ferro. Ele auxilia a digest&atilde;o e combate a constipa&ccedil;&atilde;o intestinal, al&eacute;m de melhorar a
  apar&ecirc;ncia da pele. Os tipos mais comuns no Brasil s&atilde;o o formosa e o papaya.</p>
<h3>32. Manga (<em>Mangifera indica</em>)</h3>
<figure class="image"><img alt="manga" height="419"
    src="https://static.todamateria.com.br/upload/ma/ng/manga-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ma/ng/manga-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Manga</figcaption>
</figure>
<p>Nativa da &Iacute;ndia, a manga possui quantidades significativas de a&ccedil;&uacute;car, vitaminas e minerais. Ela
  &eacute; indicada para combater anemia devido sua alta concentra&ccedil;&atilde;o de ferro.</p>
<h3>33. Mangaba (<em>Hancornia speciosa</em>)</h3>
<figure class="image"><img alt="mangaba" height="300"
    src="https://static.todamateria.com.br/upload/ma/ng/mangaba.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="600" class="lazyload" data-src="https://static.todamateria.com.br/upload/ma/ng/mangaba.jpg?auto_optimize=low"
    loading="lazy">
  <figcaption>Mangaba</figcaption>
</figure>
<p>A mangaba &eacute; uma fruta t&iacute;pica do Cerrado, possui baixa caloria e vitaminas A, C, B1 e B2, al&eacute;m de
  prote&iacute;nas, ferro, c&aacute;lcio e f&oacute;sforo. Ela auxilia no controle da press&atilde;o arterial e no
  sistema imunol&oacute;gico. Pode ser consumida in natura ou em forma de doces, sucos e sorvetes.</p>
<div id="div-gpt-sg-13ff9163a6c972bf473ada3e2fb562d4" class="ad-unit ad-unit--pt-br"><amp-ad width="336" height="280"
    type="doubleclick" data-slot="/1062898/todamateria_inarticle_mrec3" data-multi-size="300x250,250x250,200x200"
    data-enable-refresh="30"></amp-ad></div>
<h3>34. Maracuj&aacute; (<em>Passiflora edulis</em>)</h3>
<figure class="image"><img alt="maracuj&aacute;" height="449"
    src="https://static.todamateria.com.br/upload/ma/ra/maracuja-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ma/ra/maracuja-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Maracuj&aacute;</figcaption>
</figure>
<p>Amplamente encontrado em regi&otilde;es tropicais, o maracuj&aacute; &eacute; muito conhecido pelo seu poder
  calmante. Possui vitaminas A, C e do complexo B, al&eacute;m de ferro, s&oacute;dio, c&aacute;lcio e f&oacute;sforo.
  Tem um sabor &aacute;cido e pode ser consumido in natura e no preparo de sobremesas e sucos.</p>
<h3>35. Melancia (<em>Citrullus lanatus</em>)</h3>
<figure class="image"><img alt="melancia" height="569"
    src="https://static.todamateria.com.br/upload/me/la/melancia-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/me/la/melancia-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Melancia</figcaption>
</figure>
<p>Origin&aacute;ria da &Aacute;frica, a melancia &eacute; rica em &aacute;gua, o que a torna muito refrescante. Possui
  a&ccedil;&uacute;car, c&aacute;lcio, f&oacute;sforo e ferro e apresenta capacidade antioxidante e
  anti-inflamat&oacute;ria.</p>
<h3>36. Mel&atilde;o (<em>Cucumis melo</em>)</h3>
<figure class="image"><img alt="mel&atilde;o" height="420"
    src="https://static.todamateria.com.br/upload/me/la/melao-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/me/la/melao-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Mel&atilde;o amarelo</figcaption>
</figure>
<p>Origin&aacute;rio da &Aacute;frica, o mel&atilde;o &eacute; uma fruta rica em &aacute;gua e possui quantidades
  significativas de c&aacute;lcio, f&oacute;sforo e ferro. &Eacute; rico em vitamina A e C, que auxiliam na
  produ&ccedil;&atilde;o de col&aacute;geno e preven&ccedil;&atilde;o do envelhecimento.</p>
<h3>37. Morango (<em>Fragaria vesca</em>)</h3>
<figure class="image"><img alt="morango" height="315"
    src="https://static.todamateria.com.br/upload/mo/ra/morango-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/mo/ra/morango-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Morango</figcaption>
</figure>
<p>Origin&aacute;rio da Europa, o morango possui vitaminas C, A, E, B5 e B6, al&eacute;m de c&aacute;lcio,
  pot&aacute;ssio, ferro, sel&ecirc;nio e magn&eacute;sio. Essa fruta &eacute; indicada para fortalecer o sistema
  imunol&oacute;gico e processos de cicatriza&ccedil;&atilde;o. Possui um sabor adocicado e &aacute;cido, podendo ser
  consumido in natura, em sucos e no preparo de sobremesas.</p>
<h3>38. Pequi (<em>Caryocar brasiliense</em>)</h3>
<figure class="image"><img alt="pequi" height="284"
    src="https://static.todamateria.com.br/upload/pe/qu/pequi-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/pe/qu/pequi-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Pequi</figcaption>
</figure>
<p>Fruto da planta nativa s&iacute;mbolo do Cerrado, o pequizeiro. O pequi &eacute; rico em vitamina A e C, sendo
  bastante apreciado na alimenta&ccedil;&atilde;o, tanto em pratos salgados quanto doces, al&eacute;m de licores.</p>


<h3>39. Pera (<em>Pyrus communis</em>)</h3>
<figure class="image"><img alt="pera" height="478"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta39pera-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta39pera-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Pera</figcaption>
</figure>
<p>A pera &eacute; uma fruta rica em s&oacute;dio, pot&aacute;ssio, ferro, magn&eacute;sio e c&aacute;lcio. Ajuda a
  melhorar a pris&atilde;o de ventre, perder peso e controlar a diabetes. Al&eacute;m disso, ela contribui para o
  funcionamento do sistema imunol&oacute;gico.</p>
<h3>40. P&ecirc;ssego (<em>Prunus persica</em>)</h3>
<figure class="image"><img alt="p&ecirc;ssego" height="387"
    src="https://static.todamateria.com.br/upload/pe/ss/pessego-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/pe/ss/pessego-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>P&ecirc;ssego</figcaption>
</figure>
<p>O p&ecirc;ssego &eacute; uma fruta rica em antioxidantes. Ele possui os minerais f&oacute;sforo, magn&eacute;sio,
  mangan&ecirc;s, cobre, iodo e ferro, al&eacute;m de vitaminas A, C e do complexo B. Apresenta um sabor suave e
  adocicado, sendo consumido em sua forma natural ou ainda em compota.</p>
<h3>41. Pitanga (<em>Eugenia uniflora</em>)</h3>
<figure class="image"><img alt="pitanga" height="350"
    src="https://static.todamateria.com.br/upload/pi/ta/pitanga-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/pi/ta/pitanga-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Pitanga</figcaption>
</figure>
<p>A pitanga &eacute; uma fruta vermelha e de sabor adocicado e &aacute;cido. Apresenta como principais nutrientes o
  pot&aacute;ssio, sais minerais e vitamina C. Ela &eacute; indicada para artrite, diarreia, febre, gota e reumatismo.
</p>
<h3>42. Pitaya (<em>Hylocereus guatemalensis</em>)</h3>
<figure class="image"><img alt="pitaya" height="330"
    src="https://static.todamateria.com.br/upload/pi/ta/pitaya.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="620" class="lazyload" data-src="https://static.todamateria.com.br/upload/pi/ta/pitaya.jpg?auto_optimize=low"
    loading="lazy">
  <figcaption>Pitaya branca</figcaption>
</figure>
<p>Fruta ex&oacute;tica nativa da Am&eacute;rica Tropical, a pitaya apresenta uma polpa que pode ser branca ou roxa.
  Rica em prote&iacute;nas, vitamina C, ferro e c&aacute;lcio, ela possui propriedades digestivas. &Eacute; consumida in
  natura, sucos, geleias e doces.</p>
<h3>43. Pupunha (<em>Bactris gasipaes</em>)</h3>
<figure class="image"><img alt="pupunha" height="420"
    src="https://static.todamateria.com.br/upload/pu/pu/pupunha-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/pu/pu/pupunha-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Pupunha</figcaption>
</figure>
<p>T&iacute;pico da Amaz&ocirc;nia, a pupunha &eacute; uma fruta rica em prote&iacute;nas, carboidratos e minerais.
  Apresenta, ainda, alto teor de vitamina A. Seus nutrientes auxiliam no fortalecimento do sistema imunol&oacute;gico.
  Seus frutos s&atilde;o cozidos com sal antes de serem consumidos.</p>
<h3>44. Rom&atilde; (<em>Punica granatum L.</em>)</h3>
<figure class="image"><img alt="rom&atilde;" height="327"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta44roma-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta44roma-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Rom&atilde;</figcaption>
</figure>
<p>De origem asi&aacute;tica, o rom&atilde; &eacute; uma fruta vermelha com interior repleto de sementes. Com sabor
  &aacute;cido, sua casca &eacute; utilizada no preparo de ch&aacute;, auxiliando no tratamento de
  inflama&ccedil;&otilde;es bucais e garganta. As sementes podem ser consumidas cruas.</p>
<h3>45. Siriguela (<em>Spondias purp&uacute;rea</em>)</h3>
<figure class="image"><img alt="siriguela" height="420"
    src="https://static.todamateria.com.br/upload/si/ri/siriguela-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/si/ri/siriguela-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Siriguela</figcaption>
</figure>
<p>Fonte de vitaminas A, B e C, a siriguela apresenta uma rica quantidade de c&aacute;lcio, f&oacute;sforo e ferro.
  Possui sabor doce e quando madura apresenta cor avermelhada. Essa fruta &eacute; utilizada no tratamento de anemias e
  auxilia o sistema imunol&oacute;gico.</p>
<div id="div-gpt-sg-598fdf3b0501decb8d06c1ae77675921" class="ad-unit ad-unit--pt-br"><amp-ad width="336" height="280"
    type="doubleclick" data-slot="/1062898/todamateria_inarticle_mrec4" data-multi-size="300x250,250x250,200x200"
    data-enable-refresh="30"></amp-ad></div>
<h3>46. T&acirc;mara (<em>Phoenix dactylifera</em>)</h3>
<figure class="image"><img alt="t&acirc;mara" height="447"
    src="https://static.todamateria.com.br/upload/ta/ma/tamara-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ta/ma/tamara-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>T&acirc;mara</figcaption>
</figure>
<p>A t&acirc;mara tem origem no Golfo P&eacute;rsico, sendo uma fruta de sabor agridoce. Com uma cor avermelhada, ela
  &eacute; rica em carboidratos, fibras, pot&aacute;ssio, ferro e c&aacute;lcio. Ela auxilia na redu&ccedil;&atilde;o da
  press&atilde;o arterial, na sa&uacute;de dos ossos e no al&iacute;vio da pris&atilde;o de ventre.</p>
<h3>47. Tamarindo (<em>Tamarindus indica</em>)</h3>
<figure class="image"><img alt="tamarindo" height="396"
    src="https://static.todamateria.com.br/upload/ta/ma/tamarindo-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ta/ma/tamarindo-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Tamarindo</figcaption>
</figure>
<p>O tamarindo &eacute; uma fruta marrom de sabor doce e azedo. Ele &eacute; considerado um laxante natural, sendo muito
  utilizado na pris&atilde;o de ventre. Pode ser feito consumo das folhas, flores e sementes.</p>
<h3>48. Tangerina (<em>Citrus reticulata</em>)</h3>
<figure class="image"><img alt="tangerina" height="354"
    src="https://static.todamateria.com.br/upload/ta/ng/tangerina-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/ta/ng/tangerina-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Tangerina</figcaption>
</figure>
<p>A tangerina &eacute; fonte das vitaminas A e C, al&eacute;m de sais minerais, como c&aacute;lcio e f&oacute;sforo.
  Contribui para evitar problemas card&iacute;acos, colesterol alto, diabetes e hipertens&atilde;o. Seu sabor &eacute;
  &aacute;cido e adocicado, sendo utilizado com frequ&ecirc;ncia na produ&ccedil;&atilde;o de geleias.</p>
<h3>49. Tucum&atilde; (<em>Astrocaryum aculeatum</em>)</h3>
<figure class="image"><img alt="tucum&atilde;" height="340"
    src="https://static.todamateria.com.br/upload/tu/cu/tucuma-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/tu/cu/tucuma-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Tucum&atilde;</figcaption>
</figure>
<p>De origem amaz&ocirc;nica, o tucum&atilde; apresenta alto teor de vitamina A, vitamina B1 e vitamina C. Ele &eacute;
  consumido em estado natural e tamb&eacute;m &eacute; utilizado para prepara&ccedil;&atilde;o de licor e sorvetes.</p>
<h3>50. Uva verde (<em>Vitis sp.</em>)</h3>
<figure class="image"><img alt="uva" height="407"
    src="https://static.todamateria.com.br/upload/fr/ut/fruta50uva-cke.jpg?width=50&amp;auto_optimize=low&amp;blur=10"
    width="630" class="lazyload"
    data-src="https://static.todamateria.com.br/upload/fr/ut/fruta50uva-cke.jpg?auto_optimize=low" loading="lazy">
  <figcaption>Uva verde e uva roxa</figcaption>
</figure>
<p>A uva verde possui vitamina C e do complexo B, sendo uma fruta rica em ferro, c&aacute;lcio e pot&aacute;ssio. Possui
  efeito antioxidante, anti inflamat&oacute;rio e atua na preven&ccedil;&atilde;o do c&acirc;ncer.</p>

"""

# Função para gerar um valor aleatório para o preço da fruta entre 1.00 e 9.99
def generate_random_price():
    return round(random.uniform(1.00, 9.99), 2)

# Lista para armazenar os dados de cada fruta
fruits_data = []

# Criar o objeto BeautifulSoup para fazer o parse do dataset
soup = BeautifulSoup(dataset, "html.parser")

# Encontrar todos os elementos <h3>, <figure> e <p>
fruits = soup.find_all("h3")
images = soup.find_all("img")
descriptions = soup.find_all("p")

# Iterar sobre os elementos encontrados e extrair os dados de cada fruta
for i in range(len(fruits)):
    index, title_text = i+1, fruits[i].get_text().split(". ", 1)[1]
    image_url = images[i]["src"]
    description = descriptions[i].get_text()
    
    fruit_data = {
        "id": index,
        "title": title_text,
        "pictureUrl": image_url.replace("&blur=10", ""),
        "description": description.replace("\n ", ""),
        "quantity": 10,
        "price": generate_random_price()
    }
    fruits_data.append(fruit_data)

# Gerar o JSON final com base nos dados extraídos
json_data = json.dumps(fruits_data, indent=2, ensure_ascii=False)

# salva em utf8
with open("api/products.json", "w", encoding="utf8") as json_file:
    json_file.write(json_data)

print(json_data)
