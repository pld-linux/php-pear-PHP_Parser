%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Parser
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a PHP grammar parser
Summary(pl):	%{_pearname} - parser sk�adni PHP
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	387e2f91abc77dc556224cb467d7998e
URL:		http://pear.php.net/package/PHP_Parser/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

%description -l pl
PHP_Parser jest analizatorem kodu �r�d�owego bazowanym na prawdziwym
parserze wygenerowanym przez phpJay. Parser u�ywa tego samego �r�d�a
EBNF, kt�rego PHP u�ywa do sparsowania samego siebie, ma zatem takie
same mo�liwo�ci. Ta wersja w pe�ni wspiera parsowanie ka�dego elementu
PHP 5 beta 1, co obejmuje:
- klasy
- klasy abstrakcyjne
- dziedziczenie, implementacje
- interfejsy
- metody
- wyj�tki parsowane bezpo�rednio z kodu
- deklarowane zmienne statyczne (static variables)
- zmienne globalne i superglobalne ($_GET) u�yte i deklarowane
- zmienne
- sta�e
- funkcje (taka sama informacja jak w przypadku metod)
- definicje
- zmienne globalne (z pomoc� Tokenizer Lexer)
- zmienne superglobalne u�yte w kodzie globalnym
- deklaracje include

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples/,test_jay.sh,Parser/Core5.jay}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
