%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Parser
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a PHP grammar parser
Summary(pl.UTF-8):	%{_pearname} - parser składni PHP
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	53f1d8d7cdc8949ad55ea0d094342aa1
URL:		http://pear.php.net/package/PHP_Parser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear >= 4:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_Parser is a source code analysis tool based around a real Parser
generated by phpJay. The parser uses the same EBNF source that PHP
uses to parse itself, and it therefore as robust as PHP itself.
This version has full support for parsing out every re-usable element
in PHP 5 as of beta 1:
- classes
- abstract classes
- inheritance, implements
- interfaces
- methods
- exception parsing directly from source
- static variables declared
- global and superglobal ($_GET) variables used
and declared
- variables
- constants
- functions (same information as methods)
- defines
- global variables (with help of the Tokenizer Lexer)
- superglobal variables used in global code
- include statements

The output can be customized to return an array, return
objects of user-specified classes, and can also be
customized to publish each element as it is parsed, allowing
hooks into parsing to catch information.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHP_Parser jest analizatorem kodu źródłowego bazowanym na prawdziwym
parserze wygenerowanym przez phpJay. Parser używa tego samego źródła
EBNF, którego PHP używa do sparsowania samego siebie, ma zatem takie
same możliwości. Ta wersja w pełni wspiera parsowanie każdego elementu
PHP 5 beta 1, co obejmuje:
- klasy
- klasy abstrakcyjne
- dziedziczenie, implementacje
- interfejsy
- metody
- wyjątki parsowane bezpośrednio z kodu
- deklarowane zmienne statyczne (static variables)
- zmienne globalne i superglobalne ($_GET) użyte i deklarowane
- zmienne
- stałe
- funkcje (taka sama informacja jak w przypadku metod)
- definicje
- zmienne globalne (z pomocą Tokenizer Lexer)
- zmienne superglobalne użyte w kodzie globalnym
- deklaracje include

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
