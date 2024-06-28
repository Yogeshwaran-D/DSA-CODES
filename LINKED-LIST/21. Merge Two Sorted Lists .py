class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 :
            return list2
        if not list2:
            return list1
        l1=list1
        l2=list2
        while l1:
            node=l1
            l1=node.next
            temp=l2
            if temp.val>=node.val:
                node.next=l2
                l2=node
                continue
            while temp.next and temp.next.val<=node.val :
                temp=temp.next
            if not temp.next:
                temp.next=node
                node.next=None
            else:
                node.next=temp.next
                temp.next=node
        return l2