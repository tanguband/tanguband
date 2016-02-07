%define version 1.1.0b
%define release 3

Summary: tang_band %{version}
Name: tang_band
Version: %{version}
Release: %{release}
Copyright: unknown
Group: Amusements/Games
Packager: Takahiro MIZUNO <tow@plum.freemail.ne.jp>
Url: http://echizen.s5.xrea.com/heng/index.html
Source: tang_band-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
tang_band is a variant of ZAngband.

Official page is this,
http://echizen.s5.xrea.com/heng/eng-tang_band/index.html

More infomation is /usr/doc/tang_band-hoge/readme_eng.txt

Summary(ja): 短愚蛮怒 %{version}

%description -l ja
短愚蛮怒は Angband のバリアントです。

本ソフトウェアの最新版は以下の場所から入手できます。


詳しくは /usr/doc/tang_band-hoge/readme.txt を参照。

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --with-libpath=%{_datadir}/games/tang_band/lib
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/games/tang_band
cp src/tang_band $RPM_BUILD_ROOT/%{_bindir}
cp -R lib/ -p $RPM_BUILD_ROOT/%{_datadir}/games/tang_band/
touch $RPM_BUILD_ROOT/%{_datadir}/games/tang_band/lib/apex/scores.raw

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -e %{_datadir}/games/tang_band/lib/data/f_info_j.raw ]
then
rm -rf %{_datadir}/games/tang_band/lib/data/*.raw
fi
exit 0

%files
%defattr(-,root,root)
%attr(2755,root,games) %{_bindir}/tang_band
%dir %{_datadir}/games/tang_band/lib
%attr(775,root,games) %dir %{_datadir}/games/tang_band/lib/apex
%attr(775,root,games) %dir %{_datadir}/games/tang_band/lib/bone
%attr(775,root,games) %dir %{_datadir}/games/tang_band/lib/data
%dir %{_datadir}/games/tang_band/lib/edit
%dir %{_datadir}/games/tang_band/lib/file
%dir %{_datadir}/games/tang_band/lib/help
%dir %{_datadir}/games/tang_band/lib/info
%dir %{_datadir}/games/tang_band/lib/pref
%attr(775,root,games) %dir %{_datadir}/games/tang_band/lib/save
%dir %{_datadir}/games/tang_band/lib/script
%dir %{_datadir}/games/tang_band/lib/user
%dir %{_datadir}/games/tang_band/lib/xtra
%dir %{_datadir}/games/tang_band/lib/xtra/graf
%{_datadir}/games/tang_band/lib/apex/h_scores.raw
%{_datadir}/games/tang_band/lib/apex/readme.txt
%attr(664 root,games) %config(noreplace) %{_datadir}/games/tang_band/lib/apex/scores.raw
%{_datadir}/games/tang_band/lib/bone/delete.me
%{_datadir}/games/tang_band/lib/data/delete.me
%{_datadir}/games/tang_band/lib/edit/*.txt
%{_datadir}/games/tang_band/lib/file/*.txt
%{_datadir}/games/tang_band/lib/help/*.hlp
%{_datadir}/games/tang_band/lib/help/*.txt
%{_datadir}/games/tang_band/lib/info/delete.me
%{_datadir}/games/tang_band/lib/pref/*.prf
%{_datadir}/games/tang_band/lib/save/delete.me
%{_datadir}/games/tang_band/lib/script/delete.me
%{_datadir}/games/tang_band/lib/user/delete.me
%{_datadir}/games/tang_band/lib/xtra/graf/8x8.bmp
%doc readme.txt readme_angband readme_eng.txt


%changelog

* Fri Jul 05 2002 Takahiro MIZUNO <tow@plum.freemail.ne.jp>
- hengband RPM 1.0.0b release 3
- Add %preun script.
- Change source extension. (tar.gz -> bz2)
- Fix Copyright.
- Fix simply %files.
- Fix %description.

* Mon Jun 17 2002 Takahiro MIZUNO <tow@plum.freemail.ne.jp>
- hengband RPM 1.0.0b release 2
- Fix setgid permission. (Mogamiさん多謝)

* Sun Jun 16 2002 Takahiro MIZUNO <tow@plum.freemail.ne.jp>
- hengband RPM 1.0.0b release 1

* Sun Jun 16 2002 Takahiro MIZUNO <tow@plum.freemail.ne.jp> 
- hengband RPM 1.0.0 release 1

