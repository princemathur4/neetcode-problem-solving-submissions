class Solution:

    def encode(self, strs: List[str]) -> str:
        return '###' + "+++".join([
            "===" + "---".join(list(text)) + "==="
            for text in strs
        ]) + '###'

    def decode(self, s: str) -> List[str]:
        # print(f"s: `{s}`", )
        s = s.replace("###", "")
        # print("new s:", s)
        if not s:
            return []
        strs = s.split("+++")
        output = [''.join(text.replace("===", "").split("---")) for text in strs]
        return output
