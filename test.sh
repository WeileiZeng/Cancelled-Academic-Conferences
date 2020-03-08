echo start
result=`git status`

if "$result" == "On branch master Your branch is up to date with 'origin/master'. nothing to commit, working tree clean" 
then
    echo "nothing to commit. exit 0"
    exit 0
else
    echo "else"
fi

echo done
